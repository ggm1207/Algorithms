import numpy as np
import sys
import argparse
import sklearn.datasets

# mode 'coh' : 응집  'div' : 분할 
# K number : 군집 수


class DIV(): # method : K-means
    def __init__(self,data,k):
        self.data = data
        self.k = k
    
    def clustering(self):
        while True:
            self.centers = np.random.randint(0, len(self.data), self.k)
            if len(list(self.centers)) == len(list(set(self.centers))):
                break
        
        labels = [0 for i in range(len(self.data))]
        old_labels = [l for l in labels]
        i = 0
        print(self.centers)
        while(True):
            print(i)
            labels = np.array([self.nearest(d , self.centers) for d in self.data])
            if np.all(labels == old_labels):
                break
            self.update_centers(labels, self.data)
        print(data)
        print(labels)

    def nearest(self, x, centers):
         sims = [self.sim(x,c) for c in centers]
         print('sims:', sims)
         return sims.index(max(sims))
             
    def update_centers(self, labels , data):
        for i in range(self.k):
            self.centers[i] = np.mean(data[np.where(labels == i)], axis = 0)       

    def sim(self, x, y):
        print('x,y:', x, y)
        return np.dot(x,y) / (np.linalg.norm(x) * np.linalg.norm(y))

def coh(k):
    pass

def div(k):
    pass

def main():
    parser = argparse.ArgumentParser(description = 'This code is written for Algorithm-briefing about Clustering')
    parser.add_argument('--mode', type = str, default = 'div', choices = ['coh','div'],metavar = '["coh", "div"]', help = 'Choose a mode about algorithm and start!')
    parser.add_argument('--k', type = int, default = 2 , choices = [2,3,4,5], metavar = 'Choose a number of Cluster', help = 'What do you want the number of cluster?' )
    args = parser.parse_args()

    MODE = args.mode
    K = args.k
#    print(MODE, K)

    if MODE == 'coh':
        coh(K)
    else:
        div(K)

if __name__ == "__main__":
    # main()
    data = [[1,2],[2,1],[3,4],[4,3]]
    k = DIV(data,2)
    k.clustering()