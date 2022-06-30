#!/usr/bin/python3
# auther@hy
# 2022年06月30日
import  logging
# 设置打印日志的基本信息 ,总开关水平，格式中message必须要有
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(process)d- %(filename)s[line:%(lineno)d] -' \
                                              '%(levelname)s:%(message)s')
logging.debug("this is debug....")
logging.info("this is info.....")
logging.warning("this is warning.....")
logging.error("this is error.....")
logging.critical("this is critical....")
