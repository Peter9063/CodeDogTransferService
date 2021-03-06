'''
Created on 2020年11月30日

@author: Peter
'''
import threading
import traceback

import sqlalchemy
from sqlalchemy.engine import create_engine
import sqlalchemy.ext.declarative.api
from sqlalchemy.orm.session import sessionmaker

from db.utils.AbsDatabaseManager import AbsDatabaseManager
from entity.yifei.INVMB import INVMB
from utils.LoggerHelp import LoggerHelp


class MSSQLDatabaseManager(AbsDatabaseManager):
            
    def config(self,host='127.0.0.1',port='1433',database='database',user='sa',paswd='sa',charset='utf8' ,encoding='utf-8',
                    max_overflow=0,pool_size=5,pool_timeout=30,pool_recycle=-1,echo=True):
        """
        配置数据库连接参数
        """
        self.logger.info('MSSQLDatabaseManager config begin')
        self._sqlEngine=create_engine('mssql+pymssql://%s:%s@%s:%s/%s?charset=%s'%(user,paswd,host,port,database,charset),
                                encoding=encoding,
                                echo=echo,
                                max_overflow=max_overflow,  # 超过连接池大小外最多创建的连接
                                pool_size=pool_size,  # 连接池大小
                                pool_timeout=pool_timeout,  # 池中没有线程最多等待的时间，否则报错
                                pool_recycle=pool_recycle  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                                  )
        self._sqlSession=sessionmaker(bind=self._sqlEngine)
        self.logger.info('MSSQLDatabaseManager config end')
        
# if __name__=='__main__':
#     databaseManager=MSSQLDatabaseManager()
#     databaseManager.config(host='192.168.0.197',
#                                                         port='1433',
#                                                         user='sa',
#                                                         paswd='dh+2013',
#                                                         database='DHGROUP',
#                                                         charset='utf8' ,
#                                                         encoding='utf-8',
#                                                         echo=False)
#     session=databaseManager.getSession()
#     list=session.query(INVMB).all()
#     session.close()
#     for row in list:
#         print(row)