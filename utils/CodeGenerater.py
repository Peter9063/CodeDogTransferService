#数据库实体类代码生成器
import os

if __name__=='__main__':
#     try:
#         cmd = "sqlacodegen --tables INVMB mssql+pymssql://sa:dh+2013@192.168.0.197/DHGROUP > ../entity/yifei/INVMB.py"
#         os.system(cmd)
#         print('代码生成成功!')
#     except Exception as e:
#         print("代码生成器生成失败!", e)

# #数据库实体类生成器
#     import os
#     cmd = "sqlacodegen  mysql+pymysql://root:root@127.0.0.1/mytest >tmp.py"
#     os.system(cmd)

#生成指定表实体
    import os
    cmd = "sqlacodegen --tables ps mysql+pymysql://root:root@localhost:3306/bb2_default > ../entity/2box/ps.py"
    os.system(cmd)