#!/usr/bin/python3
# auther@hy
# 2022年06月24日
from contextlib import contextmanager


@contextmanager
def file_open():
    """
    上下文
    :return:
    """
    f = open()

