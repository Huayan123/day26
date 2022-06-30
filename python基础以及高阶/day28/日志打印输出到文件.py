#!/usr/bin/python3
# auther@hy
# 2022年06月30日
import logging
logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='w',
                    encoding='utf8',
                    format='%(asctime)s -%(process)d- %(filename)s[line:%(lineno)d]- %(levelname)s:%(message)s')
logging.debug("this is debug....")
logging.info("this is info....")
logging.warning("this is warning.....")
logging.error("this is error....")
logging.critical("this is critical....")

