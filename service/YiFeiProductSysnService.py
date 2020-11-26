import copy
import logging
import traceback

from sqlalchemy.sql.expression import asc, or_

from db.utils.MsSQLManager import MsSQLManager
from db.utils.MySQLManager import MySQLManager
from entity.twobox.PS import PS
from entity.twobox.PT import PT
from entity.yifei.INVMB import INVMB
from utils.LoggerHelp import LoggerHelp


class YiFeiProductSysnService():
    logger=None
    
    def __init__(self,logger=None):
        if not logger:
            self.logger= LoggerHelp.getDefaultLogger("YiFeiProductSysnService")
        else:
            self.logger=logger
    
    def updateCompare(self,sqlSession, productMapFrom2YiFei, newItem, insertList, updateList):
        """
        更新比较
        """
#         self.logger.info("compare:"+newItem.MB001+":"+str(productMapFrom2YiFei.__contains__(newItem.MB001)))
        if (productMapFrom2YiFei.__contains__(newItem.MB001)):
            invmbItem = productMapFrom2YiFei[newItem.MB001]
            invmbItem.MB002=newItem.MB002
            invmbItem.MB003=newItem.MB003
            invmbItem.MB009=newItem.MB009
            updateList.append(invmbItem)
            try:
                sqlSession.commit()
            except Exception as e:
                self.logger.error(traceback.format_exc())
        else:
            insertList.append(newItem)


    def changInvmbModel(self, row):
        """
        2box实体变换成Yifei实体
        """
        invmbItem = INVMB()
        invmbItem.FLAG=1
        invmbItem.MB001 = row[0].pn
        invmbItem.MB005="132"
        invmbItem.MB006=""
        invmbItem.MB017="1003"
        invmbItem.MB019="Y"        
        invmbItem.MB022="N"
        invmbItem.MB025="P"
        invmbItem.MB026="99"
        invmbItem.MB034="L"
        invmbItem.MB040=0
        invmbItem.MB042="1"
        invmbItem.MB043="2"
        invmbItem.MB044="N"
        invmbItem.MB047=0 #标准售价
        invmbItem.MB051=0 #零售价
        invmbItem.MB052="N"
        invmbItem.MB057=0 #单位标准材料成本
        invmbItem.MB064=0 #库存数量 
        invmbItem.MB065=0
        invmbItem.MB066="N"
        invmbItem.MB080=""
        invmbItem.MB102="N"
        invmbItem.MB109="Y"
        invmbItem.MB111=0.13
        invmbItem.MB436="1"
        invmbItem.MB442="2"
        invmbItem.MB443="0"
        
        if row[0].mn!=None and len(row[0].mn)>25:
            invmbItem.MB003=row[0].mn[0:25]
        
        if(row[0].unit!=None):
            invmbItem.MB004=row[0].unit
            
        if row[0].ed!=None and len(row[0].ed)>25:
            invmbItem.MB002=row[0].ed[0:25]
            invmbItem.MB009=row[0].ed[0:110]
            
        if(row[0].make_buy!=None and len(row[0].make_buy)>=3):
            if row[0].make_buy.find("BUY")>=0 or row[0].make_buy.find("X")>=0 or row[0].make_buy.find("MAKE"):
                invmbItem.MB025="M"
        if invmbItem.MB001.find("CA")>=0 or invmbItem.MB001.find("BA")>=0:
            invmbItem.MB025="M"
        
        if invmbItem.MB001!=None and (invmbItem.MB001.find("CA") or invmbItem.MB001.find("BA")) :
            invmbItem.MB005="122"
            invmbItem.MB017="0101"

        if(row[0].po_unit_rate!=None and row[0].po_unit_rate>0):
            invmbItem.MB040=row[0].po_unit_rate
            
        if row[0].po_unit!=None:
            invmbItem.MB148=str(row[0].po_unit)
            invmbItem.MB149=str(row[0].po_unit)
#         if row[0].min_qty!=None:
#             invmbItem.UDF51=row[0].min_qty

        return invmbItem


    def copyModel(self, invmbItem, invmbItem06):
        """
        实体值复制
        """
        for key in invmbItem.__dict__:
            if key != '_sa_instance_state':
                setattr(invmbItem06, key, getattr(invmbItem, key))

    def dongYuProductSysn(self):
        """
       东宇产品信息同步
        """
        self.logger.info('dongYuProductSysn begin')
        mySqlSession=MySQLManager.getInstance().getSession()
        productListFrom2Box=mySqlSession.query(PS,PT).outerjoin(PT,PS.pn==PT.pn).filter(PS.isdeleted==0).order_by(asc(PS.pn)).all()
        self.logger.info("加载2Box产品数据%s条"%str(len(productListFrom2Box)))
        
        msSqlSession=MsSQLManager.getInstance().getSession()
#         productListFrom2YiFei=msSqlSession.query(INVMB).filter(or_(INVMB.MB005==132, INVMB.MB005==122)).order_by(asc(INVMB.MB001)).all()
        productListFrom2YiFei=msSqlSession.query(INVMB).order_by(asc(INVMB.MB001)).all()
        self.logger.info("加载YiFei产品数据%s条"%str(len(productListFrom2YiFei)))
        productMapFrom2YiFei={}
        for row in productListFrom2YiFei:
            productMapFrom2YiFei[row.MB001.strip()]=row
            

        insertList=[]
        updateList=[]
        for row in productListFrom2Box:
            invmbItem = self.changInvmbModel(row)
            if invmbItem.MB001.find("CA")>=0:
                self.updateCompare(msSqlSession,productMapFrom2YiFei, invmbItem, insertList, updateList)
                invmbItem06=INVMB()
                self.copyModel(invmbItem, invmbItem06)
                invmbItem06.MB001="06%s"%invmbItem06.MB001
                invmbItem06.MB080= invmbItem06.MB001 #货号，通过货号取得采购单品号；
                invmbItem06.MB005="112"
                invmbItem06.MB017="0101"
                invmbItem06.MB025="P"
                self.updateCompare(msSqlSession,productMapFrom2YiFei, invmbItem06, insertList, updateList)
            else:
                self.updateCompare(msSqlSession,productMapFrom2YiFei, invmbItem, insertList, updateList)
        
        self.logger.info("需要新增保存%s条."%str(len(insertList)))
        for row in insertList:
            try:
                self.logger.info("save:%s"%row.MB001)
                self.logger.info(row)
                msSqlSession.add(row)
                msSqlSession.commit()
            except Exception as e:
                self.logger.error(traceback.format_exc())
        self.logger.info("需要更新保存%s条."%str(len(updateList)))
        
        msSqlSession.close()
        mySqlSession.close()
        self.logger.info('dongYuProductSysn end')
            
# if __name__=='__main__':
#     MsSQLManager.getInstance().config(host='192.168.1.52',
#                                                             port='1433',
#                                                             user='sa',
#                                                             paswd='dh+2013',
#                                                             database='DHGROUP',
#                                                             charset='utf8' ,
#                                                             encoding='utf-8',
#                                                             echo=True)
#     MySQLManager.getInstance().config(host='127.0.0.1',
#                                                         port='3306',
#                                                         user='root',
#                                                         paswd='root',
#                                                         database='bb2_default',
#                                                         charset='utf8' ,
#                                                         encoding='utf-8',
#                                                         echo=False)
#   
#     productSysnService=YiFeiProductSysnService()
#     productSysnService.dongYuProductSysn()