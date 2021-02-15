## TransferService##

B.安装说明

	1.python环境要求:
		pip install pypiwin32
		pip install APScheduler
		pip install WMI
		pip install pymysql
		pip install pymssql
		pip install SQLAlchemy
		
	2.服务的安装：
		python 【TransferService.py】 install
	3. 服务卸载：
		python 【TransferService.py】 remove
	4.环境变量
	  C:\Python37\Lib\site-packages\win32;C:\Python37\Lib\site-packages\pywin32_system32;C:\Python37\Scripts\;C:\Python37\;
	5.vbox api安装
		a.安装vbox v6.0.16以下安装文件;
		b.进入C:\Program Files\Oracle\VirtualBox\sdk\install;运行python vboxapisetup.py install;