import threading

from db.utils.MYSQLDatabaseManager import MYSQLDatabaseManager
from entity.twobox.PS import PS


class MySQLManager(MYSQLDatabaseManager):
    
    _instance_lock = threading.Lock()
    @classmethod
    def getInstance(cls,*args, **kwargs):
        """
        内部构造函数
        """
        if not hasattr(MySQLManager, "_instance"):
            with MySQLManager._instance_lock:
                if not hasattr(MySQLManager, "_instance"):
                    MySQLManager._instance = MySQLManager(*args, **kwargs)
        return MySQLManager._instance
    
# if __name__=='__main__':
#     MySQLManager.getInstance().config("127.0.0.1", "3306", "bb2_default", "root", "root")
#     session=MySQLManager.getInstance().getSession()
#     list=session.query(PS).all()
#     session.close()
#     for row in list:
#         print(row)