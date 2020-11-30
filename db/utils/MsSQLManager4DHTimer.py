'''
Created on 2020年11月30日

@author: Peter
'''
import threading

from db.utils.MSSQLDatabaseManager import MSSQLDatabaseManager


class MsSQLManager4DHMeter(MSSQLDatabaseManager):

    _instance_lock = threading.Lock()
    @classmethod
    def getInstance(cls,*args, **kwargs):
        """
        内部构造函数
        """
        if not hasattr(MsSQLManager4DHMeter, "_instance"):
            with MsSQLManager4DHMeter._instance_lock:
                if not hasattr(MsSQLManager4DHMeter, "_instance"):
                    MsSQLManager4DHMeter._instance = MsSQLManager4DHMeter(*args, **kwargs)
        return MsSQLManager4DHMeter._instance