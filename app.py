"""
       框架搭建:
          核心 ：api + case + data
              ————api：封装请求业务(requests)
              ————case: 集成 unittest 实现 ，调用 api 以及参数化解析 data
              ————data：封装测试数据
          报告： report + tools +run_suite.py
               —————report：保存测试报告
               —————tools：封装工具文件
               —————run_suite.py:组织测试套件

          配置：app.py
               —————app.py：封装程序常亮以及配置信息


          日志：log
                —————log：保存日志文件
"""
import logging
import logging.handlers
import os

from Tools.scripts.serve import app

"""封装接口的 URL 前缀"""
BASE_URL = "http://182.92.81.159"
"""封装项目路径"""

FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)
print("动态获取的项目绝对路径", PRO_PATH)

# 定义一个变量

TOKEN = None
USER_ID = None


# 日志模块实现
# A 配置日志，默认的日志配置 不能满足需求
def my_log_config():
    # 1.获取日志对象
    logger = logging.getLogger()
    # 2.配置输出级别 --info 以及以上
    logger.setLevel(logging.INFO)
    # 3.配置输出目标--控制台和磁盘文件
    to_1 = logging.StreamHandler()
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/mylog.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=14,
                                                     encoding="utf-8")
    # 4.组织配置并添加进日志对象--年月日时分秒 用户 级别 。。。。
    formatter = logging.Formatter(

        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 5组织配置并添加日志对象
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)


# B  调用，在需要的位置调用日志输出
# my_log_config()
# logging.info("123")
# logging.warning("123123")
