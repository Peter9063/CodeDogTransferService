from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from db.utils.AbsDatabaseManager import AbsDatabaseManager
from entity.twobox.PS import PS

class MYSQLDatabaseManager(AbsDatabaseManager):
    
    def config(self,host='127.0.0.1',port='3306',database='database',user='root',paswd='root',charset='utf8' ,encoding='utf-8',
        max_overflow=0,pool_size=5,pool_timeout=30,pool_recycle=-1,echo=True):
        """
        配置数据库连接参数
        """
        self.logger.info('MsSQLManager config begin')
        self._sqlEngine=create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=%s'%(user,paswd,host,port,database,charset),
                                encoding=encoding,
                                echo=echo,
                                max_overflow=max_overflow,  # 超过连接池大小外最多创建的连接
                                pool_size=pool_size,  # 连接池大小
                                pool_timeout=pool_timeout,  # 池中没有线程最多等待的时间，否则报错
                                pool_recycle=pool_recycle  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                                  )
        self._sqlSession=sessionmaker(bind=self._sqlEngine)
        self.logger.info('MsSQLManager config end')
        
# if __name__=='__main__':
#     databaseManager=MYSQLDatabaseManager()
#     databaseManager.config("127.0.0.1", "3306", "bb2_default", "root", "root")
#     session=databaseManager.getSession()
#     list=session.query(PS).all()
#     session.close()
#     for row in list:
#         print(row)