'''
Created on 2020年11月30日

@author: Peter
'''
import threading

from db.utils.MSSQLDatabaseManager import MSSQLDatabaseManager


class MsSQLManager4DHTimer(MSSQLDatabaseManager):

    _instance_lock = threading.Lock()
    @classmethod
    def getInstance(cls,*args, **kwargs):
        """
        内部构造函数
        """
        if not hasattr(MsSQLManager4DHTimer, "_instance"):
            with MsSQLManager4DHTimer._instance_lock:
                if not hasattr(MsSQLManager4DHTimer, "_instance"):
                    MsSQLManager4DHTimer._instance = MsSQLManager4DHTimer(*args, **kwargs)
        return MsSQLManager4DHTimer._instance