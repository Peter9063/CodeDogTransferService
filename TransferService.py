from array import array
import configparser
from datetime import datetime
from distutils.command.config import config
import logging
from logging.handlers import RotatingFileHandler
import os 
import sys
import traceback

from apscheduler.schedulers.background import BackgroundScheduler
import pythoncom
import servicemanager
import win32event
import win32service 
import win32serviceutil 
import winerror

from db.utils.MsSQLManager import MsSQLManager
from db.utils.MsSQLManager4DHMeter import MsSQLManager4DHTimer
from db.utils.MySQLManager import MySQLManager
from service.DongHaiTimerProductSysnService import DongHaiTimerProductSysnService
from service.YiFeiProductSysnService import YiFeiProductSysnService


# import time 
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# import wmi
# from entity.ServiceBackuper import ServiceBackuper
#from sqlalchemy.sql.expression import false
#东海运维守护进程
class TransferService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TransferService"
    _svc_display_name_ = "CodeCdog Transfer Service"
    _svc_description_ = "Transfer Service" 
    config=None
    logger=None
    services={}
    
    
    #初始化
    def __init__(self, args):
        if args!=None and len(args)>0:
            win32serviceutil.ServiceFramework.__init__(self, args)
            self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
            self.run = True
        self.config=self.getConfig("config.ini")
        logRoot=self.config.get("logs", "logRoot")
        logFile=self.config.get("logs", "logFile")
        logLevel=self.config.get("logs", "logLevel")
        logFormatter=self.config.get("logs", "logFormatter")
        self.logger=self.getLogger(logRoot,logFile,logLevel,logFormatter)
        
        #数据库配置
        MsSQLManager.getInstance().config(host=self.config.get("mssqlconfig","host"),
                                                                port=self.config.get("mssqlconfig","port"),
                                                                user= self.config.get("mssqlconfig","user"),
                                                                paswd=self.config.get("mssqlconfig","paswd"),
                                                                database=self.config.get("mssqlconfig","database"),
                                                                charset=self.config.get("mssqlconfig","charset"),
                                                                encoding=self.config.get("mssqlconfig","encoding"),
                                                                echo=False)
        MySQLManager.getInstance().config(host=self.config.get("mysqlconfig","host"),
                                                                port=self.config.get("mysqlconfig","port"),
                                                                user= self.config.get("mysqlconfig","user"),
                                                                paswd=self.config.get("mysqlconfig","paswd"),
                                                                database=self.config.get("mysqlconfig","database"),
                                                                charset=self.config.get("mysqlconfig","charset"),
                                                                encoding=self.config.get("mysqlconfig","encoding"),
                                                                echo=False)
        MsSQLManager4DHTimer.getInstance().config(host=self.config.get("mssqlconfig4DHTimer","host"),
                                                        port=self.config.get("mssqlconfig4DHTimer","port"),
                                                        user= self.config.get("mssqlconfig4DHTimer","user"),
                                                        paswd=self.config.get("mssqlconfig4DHTimer","paswd"),
                                                        database=self.config.get("mssqlconfig4DHTimer","database"),
                                                        charset=self.config.get("mssqlconfig4DHTimer","charset"),
                                                        encoding=self.config.get("mssqlconfig4DHTimer","encoding"),
                                                        echo=False)
        self.services["YiFeiProductSysnService"]=YiFeiProductSysnService(self.logger)
        self.services["DongHaiTimerProductSysnService"]=DongHaiTimerProductSysnService(self.logger)
        
                
        
     
     #加载配置文件
    def getConfig(self,configFile):
#         dirpath = os.path.abspath(os.path.realpath(sys.executable))
        dirpath=os.path.realpath(__file__)
        dirpath=os.path.split(dirpath)
        dirpath=dirpath[0]+'\ini'
        parser = configparser.RawConfigParser()
        parser.optionxform=str#参数键名称不再转成小写
        os.chdir(dirpath)
        parser.read(configFile)
        return parser
    
    #获取日志器
    def getLogger(self,loggerName,logFile,logLevel,logFormatter):
        if loggerName==None or loggerName=='':
            loggerName='main'
        if logFile==None or logFile=='':
            logFile='logs.log'
        if logLevel==None or logLevel=='':
            logLevel='info'
        if logFormatter==None or logFormatter=='':
            logFormatter='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        
        logger = logging.getLogger(loggerName)  
#         appDir = os.path.abspath(os.path.realpath(sys.executable))
        appDir=os.path.realpath(__file__)
        appDir=os.path.split(appDir)
        appDir=appDir[0]
        tempDir=os.path.split(logFile)
        if len(tempDir)>1:
            if tempDir[0].find(':')>0:
                appDir=tempDir[0]
                logFile=tempDir[1]
            else:
                appDir=appDir+"\\"+tempDir[0]
                logFile=tempDir[1]
#         handler = logging.FileHandler(os.path.join(appDir,logFile))
        handler =RotatingFileHandler(os.path.join(appDir,logFile), maxBytes=1024*1024*100, backupCount=5,encoding="utf-8",delay=False)
        
#         formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        formatter = logging.Formatter(logFormatter)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler =logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        if 'CRITICAL'==logLevel:
            logger.setLevel(logging.CRITICAL)
        elif 'ERROR'==logLevel:
            logger.setLevel(logging.ERROR)
        elif 'WARNING'==logLevel:
            logger.setLevel(logging.WARNING)
        elif 'INFO'==logLevel:
            logger.setLevel(logging.INFO)
        elif 'NOTSET'==logLevel:
            logger.setLevel(logging.NOTSET)
        else:
            logger.setLevel(logging.DEBUG)
        return logger
        
    #服务启动入口
    def SvcDoRun(self):
        self.logger.info('Service is run....');
        try:
            self.scheduler = BackgroundScheduler(logger=self.logger)
            if(self.config.get('task','periodFailure')!=None and self.config.get('task','periodFailure')=='true'):
                 self.scheduler.add_job(self.runTask, trigger='interval',coalesce=True, misfire_grace_time=3600, hours=1)
                 self.logger.info('Failure Setup')
            else:
                if(self.config.get('task','period')=='cron'):
                    self.scheduler.add_job(self.runTask, trigger='cron',coalesce=True, misfire_grace_time=3600, day_of_week='*', hour=self.config.get('task','periodHour'),minute=self.config.get('task','periodMinute')) 
                else:
                    self.scheduler.add_job(self.runTask, trigger='cron', day_of_week='mon-sun',coalesce=True, misfire_grace_time=3600, hour=23,minute=30)
                
            self.logger.info('scheduler is run....');
            self.scheduler.start()
            self.logger.info(self.scheduler.get_jobs())
            self.logger.info('scheduler is close....');
        except Exception as e:
            self.logger.error(traceback.format_exc())
        self.logger.info( win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE))
           
       
     #服务关闭入口   
    def SvcStop(self):
        try:
            self.logger.info('Service is stop....');
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            win32event.SetEvent(self.hWaitStop)
            self.scheduler.shutdown(True)
        except Exception as e:
            self.logger.error(traceback.format_exc())
    
    def runTask(self):
            runFlag=True
            try:
                if(self.config.get('task','periodFailure')!=None and 
                   self.config.get('task','periodFailure')=='true' ):
                    if(str(datetime.now().hour)==self.config.get('task','periodHour')):
                        self.logger.info('wark up : %s' % datetime.now())
                        runFlag=True
                else:
                     runFlag=True
                if(runFlag==True):
                    self.logger.info('runTask begin! The time is: %s' % datetime.now())
                    try:
                        self.services["YiFeiProductSysnService"].dongYuProductSysn()
                        self.services["DongHaiTimerProductSysnService"].productSysn()
                    except Exception as e:   
                        self.logger.error(traceback.format_exc())
                    self.logger.info('runTask finished! The time is: %s' % datetime.now())
            except Exception as e:   
                 self.logger.error(traceback.format_exc())
                 
            
if __name__=='__main__':
#     dhOperationService=TransferService(None)
#     dhOperationService.runTask()
# 正式的程序
    if len(sys.argv) == 1:
        try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(TransferService)
            servicemanager.Initialize('TransferService', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(TransferService)