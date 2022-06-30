#!/usr/bin/python3
# auther@hy
# 2022年06月30日
import logging
logger = logging.getLogger()
# 设置总开关
logger.setLevel(logging.DEBUG)
# 设置打印日志的文件
log_file = 'log.txt'
# 设置文件句柄
fh = logging.FileHandler(log_file,mode='a')
fh.setLevel(logging.DEBUG)
# 设置控制台句柄
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
# 定义输出的message格式
fromatter = logging.Formatter("%(%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
ch.setFormatter(fromatter)
fh.setFormatter(fromatter)
# 将logger添加到hander中
logger.addHandler(fh)
logger.addHandler(ch)
logger.debug("this is debug...")
logger.info("this is info....")
logger.warning("this is warning....")
logger.error("this is error....")

