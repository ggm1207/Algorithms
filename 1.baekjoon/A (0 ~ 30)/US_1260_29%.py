import sys
import copy

MIS = lambda: map(int,input().split())

class DFS():
    def __init__(self, M_list, firstnode):
        self.M_list = M_list
        self.node = firstnode
        lists = self.getnextnode(self.node)

    def getnextnode(self, firstnode):
        if len(self.M_list) == 0:
            return []
        lists = []
        final = [y if (firstnode == x) else 0 for x, y in self.M_list]
        final = list(set(final))
        for x, y in self.M_list:
            if firstnode == x:
                final.append(y)

        

if __name__ == "__main__":
    N , M , V = MIS() # 정점, 간선, 탐색
    M_list = [list(MIS()) for i in range(M)]    
    DFS(M_list, V)

