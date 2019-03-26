import sys
import copy

MIS = lambda: map(int,input().split())

class DFS(): # Depth First Search
    def __init__(self, M_list, firstnode):
        self.M_list = M_list
        self.node = firstnode
        self.lists = []
        self.getnextnode(firstnode)
        print(self.lists)

    def getnextnode(self, firstnode): # 리스트 반환
        if len(self.M_list) == 0:
            return
        M = []
        self.lists.append(firstnode)
        # print('firstnode: ',firstnode)
        lists = list(set([y if (firstnode == x) else M.append((x,y)) for x, y in self.M_list]))
        lists = list(filter(None, lists))
        self.M_list = M
        for i in lists:
            self.getnextnode(i)
    
class BFS(): # Depth First Search
    def __init__(self, M_list, firstnode):
        self.M_list = M_list
        self.node = firstnode
        self.lists = []
        self.getnextnode(firstnode)
        print(self.lists)

    def getnextnode(self, firstnode): # 리스트 반환
        if len(self.M_list) == 0:
            return
        M = []
        self.lists.append(firstnode)
        # print('firstnode: ',firstnode)
        lists = list(set([y if (firstnode == x) else M.append((x,y)) for x, y in self.M_list]))
        lists = list(filter(None, lists))
        self.M_list = M
        for i in lists:
            self.getnextnode(i)
# 으악 헷갈린다!!


if __name__ == "__main__":
    N , M , V = MIS() # 정점, 간선, 탐색
    M_list = [list(MIS()) for i in range(M)]    
    DFS(M_list, V)

