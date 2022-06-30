#!/usr/bin/python3
# auther@hy
# 2022年06月14日
import random

MAXKEY = 1000
def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
    if g:
        h ^= g >> 24
        h &= ~g
    return h % MAXKEY

if __name__=="__main__":
      str_list = ["xiongda", "lele", "hanmeimei", "wangdao", "fenghua"]
      hash_table = [None]*MAXKEY
      for i in str_list:
          hash_table[elf_hash(i)]=i




