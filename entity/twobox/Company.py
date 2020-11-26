# create_table_orm.py
from sqlalchemy import Column, String, INTEGER, DateTime
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()
# 定义学生对象
class Company(BASE):
    # 表的名字:STUDENT
    __tablename__ = 'tab_company'
    # id
    id = Column(INTEGER,primary_key=True)
    # 表号
    name = Column(String(20))
    #创建时间
    createTime=Column(DateTime)
    #创建人
    createUser=Column(String(50))
    
    # 创建表的参数
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    
    def __str__(self):  # 格式输出查询出的数据
        return '%s,%s,%s,%s' % (self.id, self.name,self.createTime,self.createUser)
 
