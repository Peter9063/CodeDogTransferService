import threading
from db.utils.MSSQLDatabaseManager import MSSQLDatabaseManager
from entity.yifei.INVMB import INVMB

class MsSQLManager(MSSQLDatabaseManager):
    
    _instance_lock = threading.Lock()
    @classmethod
    def getInstance(cls,*args, **kwargs):
        """
        内部构造函数
        """
        if not hasattr(MsSQLManager, "_instance"):
            with MsSQLManager._instance_lock:
                if not hasattr(MsSQLManager, "_instance"):
                    MsSQLManager._instance = MsSQLManager(*args, **kwargs)
        return MsSQLManager._instance
    
# if __name__=='__main__':
#     MsSQLManager.getInstance().config(host='192.168.0.197',
#                                                         port='1433',
#                                                         user='sa',
#                                                         paswd='dh+2013',
#                                                         database='DHGROUP',
#                                                         charset='utf8' ,
#                                                         encoding='utf-8',
#                                                         echo=False)
#     session=MsSQLManager.getInstance().getSession()
#     list=session.query(INVMB).all()
#     session.close()
#     for row in list:
#         print(row)