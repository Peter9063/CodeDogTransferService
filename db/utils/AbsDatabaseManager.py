import abc
import threading
import traceback

import sqlalchemy.ext.declarative.api

from utils.LoggerHelp import LoggerHelp


class AbsDatabaseManager(metaclass=abc.ABCMeta):
    logger=None
    _instance_lock = threading.Lock()
    _sqlEngine=None
    _sqlSession=None
     
    def __init__(self,logger=None):
        if not logger:
            self.logger= LoggerHelp.getDefaultLogger(self.__class__.__name__)
        else:
            self.logger=logger
    

    @abc.abstractmethod
    def getInstance(self,cls,*args, **kwargs):
        pass
    
    @abc.abstractmethod 
    def config(self,host='127.0.0.1',port='3306',database='database',user='root',paswd='root',charset='utf8' ,encoding='utf-8',
                    max_overflow=0,pool_size=5,pool_timeout=30,pool_recycle=-1,echo=True):
        pass
            
    def getSession(self):
        """
        获取数据库session
        """
        session=None
        if self._sqlEngine!=None:
            session=self._sqlSession()
        return session
    
    def model2Table(self,model=None):
        """
        按实体创建数据库表
        """
        returnValue=False
        if model!=None and model.__class__==sqlalchemy.ext.declarative.api.DeclarativeMeta and self._sqlEngine!=None :
            try:
                model.metadata.create_all(self._sqlEngine)
                returnValue=True
            except Exception as e:
                returnValue=False
                self.logger.error(traceback.format_exc())
        return returnValue
            
            
            