#!/usr/bin/python3
# auther@hy
# 2022年06月12日
class Node:
    def __init__(self,ele = -1,lchild=None,rchild=None):
        self.ele = ele
        self.rchild = rchild
        self.lchild = lchild

class Tree:
    def __init__(self):
        self.queue = []
        self.root = None

    def build(self,ele):
        new_node = Node(ele)
        self.queue.append(new_node)
        if self.root is None:
            self.root = new_node
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                 self.queue[0].rchild = new_node
            self.queue.pop(0)
    def preorder(self,node):
        if node:
            print(node.ele,end='')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def midpreorder(self,node):
        if node:
            self.preorder(node.lchild)
            print(node.ele,end='')
            self.preorder(node.rchild)
    def lastpreoder(self,node):
        if node:
            self.lastpreoder(node.lchild)
            self.lastpreoder(node.rchild)
            print(node.ele,end='')
if __name__=='__main__':
    tree = Tree()
    for i in 'dacdfghijk':
        tree.build(i)
    # tree.preorder(tree.root)
    # print()
    tree.midpreorder(tree.root)
    print()
