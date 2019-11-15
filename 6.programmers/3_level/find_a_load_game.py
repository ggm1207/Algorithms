"""길 찾기 게임(https://programmers.co.kr/learn/courses/30/lessons/42892)
nodeinfo	                                                result
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
"""
import sys

sys.setrecursionlimit(100000)

class Node(object):
    def __init__(self, data):
        self.idx = data[0] + 1
        self.xy = data[1]
        self.left = self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data[1][0] <= node.xy[0]:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def preorder(self):
        self.pre = []
        self.pre.append(self.root.idx)
        self._preorder_value(self.root.left)
        self._preorder_value(self.root.right)

    def _preorder_value(self, node):
        if node is None:
            return
        else:
            self.pre.append(node.idx)
            self._preorder_value(node.left)
            self._preorder_value(node.right)

    def postorder(self):
        self.post = []
        self._postorder_value(self.root.left)
        self._postorder_value(self.root.right)
        self.post.append(self.root.idx)

    def _postorder_value(self, node):
        if node is None:
            return
        else:
            self._postorder_value(node.left)
            self._postorder_value(node.right)
            self.post.append(node.idx)

    def get_list(self):
        self.postorder()
        self.preorder()
        return [self.pre, self.post]
        
def solution(nodeinfo):
    index = [i for i in range(len(nodeinfo))]

    nodeinfo, index = zip(*sorted(zip(nodeinfo, index), key=lambda x: x[0][1], reverse=True))
    a = Tree()
    for idx, node in zip(index, nodeinfo):
        a.insert((idx,node))

    result = a.get_list()
    return result

if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    index = [i for i in range(len(nodeinfo))]

    nodeinfo, index = zip(*sorted(zip(nodeinfo, index), key=lambda x: x[0][1], reverse=True))
    a = Tree()
    for idx, node in zip(index, nodeinfo):
        a.insert((idx,node))

    result = a.get_list()
    print(result)