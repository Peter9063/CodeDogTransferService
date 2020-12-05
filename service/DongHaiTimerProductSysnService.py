"""
定时器数据同步
"""
import traceback

from sqlalchemy.sql.expression import asc

from db.utils.MsSQLManager import MsSQLManager
from db.utils.MsSQLManager4DHMeter import MsSQLManager4DHTimer
from entity.yifei.INVMB import INVMB
from utils.LoggerHelp import LoggerHelp


class DongHaiTimerProductSysnService():
    logger=None
    
    def __init__(self,logger=None):
        if not logger:
            self.logger= LoggerHelp.getDefaultLogger("YiFeiProductSysnService")
        else:
            self.logger=logger
            
    def updateCompare(self,sqlSession, productMapFromdhGroup, newItem, insertList, updateList):
        """
        更新比较
        """
#         self.logger.info("compare:"+newItem.MB001+":"+str(productMapFrom2YiFei.__contains__(newItem.MB001)))
        if (productMapFromdhGroup.__contains__(newItem.MB001)):
                
            invmbItem = productMapFromdhGroup[newItem.MB001]
            self.copyModel(newItem, invmbItem)
            updateList.append(invmbItem)
            self.logger.info("更新:%s记录"%invmbItem.MB001)
            try:
                sqlSession.commit()
            except Exception as e:
                self.logger.error(traceback.format_exc())
        else:
            insertList.append(newItem)
            
    def copyModel(self, sourceItem, targetItem,needChange=False):
        """
        实体值复制,needChange,mssql取出来的字符值取要转变格式;
        """
        for key in sourceItem.__dict__:
            if key != '_sa_instance_state':
                if needChange==True:
                    if type(getattr(sourceItem, key))=="".__class__:
                        setattr(targetItem, key, getattr(sourceItem, key).encode('latin-1').decode('gbk'))#转换msql字符串格式
                    else:
                        setattr(targetItem, key, getattr(sourceItem, key))
                else:
                    setattr(targetItem, key, getattr(sourceItem, key))

    def productSysn(self):
        self.logger.info('DHTimer product sysn begin')
        dhTimeSession=MsSQLManager4DHTimer.getInstance().getSession()
        productListFromdhTime=dhTimeSession.query(INVMB).filter(INVMB.MB025.in_({"M","S","P"})).order_by(asc(INVMB.MB001)).all()
        self.logger.info("定时器产品%s条"%str(len(productListFromdhTime)))

        dhGRoupSqlSession=MsSQLManager.getInstance().getSession()
        productListFromdhGroup=dhGRoupSqlSession.query(INVMB).order_by(asc(INVMB.MB001)).all()
        self.logger.info("加载集团产品数据%s条"%str(len(productListFromdhGroup)))
        productMapFromdhGroup={}
        for row in productListFromdhGroup:
            productMapFromdhGroup[row.MB001.strip()]=row
        
        insertList=[]
        updateList=[]
        for row in productListFromdhTime:
            
            invmbItem = INVMB()
            self.copyModel(row, invmbItem,True)
            invmbItem.MB001=invmbItem.MB001.strip()
            invmbItem.MB017="0101"
            invmbItem.MB005="121"
            
            if invmbItem.MB001.find("11")==0:
                invmbItem.MB005="131"
                self.updateCompare(dhGRoupSqlSession,productMapFromdhGroup, invmbItem, insertList, updateList)
                invmbItem03=INVMB()
                self.copyModel(invmbItem, invmbItem03)
                invmbItem03.MB080= invmbItem03.MB001 #货号，通过货号取得采购单品号；
                invmbItem03.MB001="03%s"%invmbItem03.MB001
                invmbItem03.MB005="111" #111定时器成品；121定时器配件;131定时器原材料
                self.updateCompare(dhGRoupSqlSession,productMapFromdhGroup, invmbItem03, insertList, updateList)
            else:
                self.updateCompare(dhGRoupSqlSession,productMapFromdhGroup, invmbItem, insertList, updateList)
        
                
        self.logger.info("需要新增保存%s条."%str(len(insertList)))
        for row in insertList:
            try:
                self.logger.info("保存:%s记录"%row.MB001)
                dhGRoupSqlSession.add(row)
                dhGRoupSqlSession.commit()
            except Exception as e:
                self.logger.error(traceback.format_exc())
        self.logger.info("需要更新保存%s条."%str(len(updateList)))
        
        dhTimeSession.close()
        dhGRoupSqlSession.close()
        self.logger.info('DHTimer product sysn end')

# if __name__=='__main__':
#     MsSQLManager.getInstance().config(host='192.168.0.197',
#                                                             port='1433',
#                                                             user='sa',
#                                                             paswd='dh+2013',
#                                                             database='DHGPTEST',
#                                                             charset='utf8' ,
#                                                             encoding='utf-8',
#                                                             echo=True)
#     MsSQLManager4DHTimer.getInstance().config(host='192.168.0.197',
#                                                             port='1433',
#                                                             user='sa',
#                                                             paswd='dh+2013',
#                                                             database='DH',
#                                                             charset='utf8' ,
#                                                             encoding='utf-8',
#                                                             echo=True)
#    
#     productSysnService=DongHaiTimerProductSysnService()
#     productSysnService.productSysn()    