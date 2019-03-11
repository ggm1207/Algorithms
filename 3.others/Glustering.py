import numpy as np
import sys
import argparse
# import sklearn.datasets
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from time import sleep

# mode 'coh' : 응집  'div' : 분할 
# K number : 군집 수

class DIV(): # method : K-means
    def __init__(self,data,k):
        self.data = np.array(data)
        self.k = k
    
    def clustering(self):
        self.centers = self.data[np.random.randint(0, len(self.data), self.k)]
            # for i in range(len(self.k)):
            #     self.centers = self.data[]
        
        labels = np.random.choice([0, 1], self.k)
        old_labels = [l for l in labels]
        
        label_set = []
        center_set = []
        # data_set = []
        
        while(True):
            self.labels = np.array([self.nearest(d , self.centers) for d in self.data])
            # print('labels:',labels)
            # print('o_labels:',old_labels)
            label_set.append(self.labels)
            center_set.append(self.centers)
            if np.all(self.labels == old_labels):
                break
            else:
                old_labels = np.copy(self.labels)
                self.update_centers()
        
        # print(data)
        # print(self.labels)

        # self.visualize()
        self.animations(self.data,label_set,center_set)

    def nearest(self, x, centers):
        # print('centers:', centers)
        sims = [self.sim(x,c) for c in centers]
        # print('sims:', sims)
        return sims.index(min(sims))
             
    def update_centers(self):
        # print('centers:',self.centers)
        for i in range(self.k):
            self.centers[i] = np.mean(self.data[np.where(self.labels == i)], axis = 0)       

    def sim(self, x, y):
        # print('x,y:', x, y)
        a, b = x
        c, d = y
        uclid = math.sqrt((a - c)*(a-c) + (b-d)*(b-d ))
        #return np.dot(x,y) / (np.linalg.norm(x) * np.linalg.norm(y))
        return uclid

    def visualize(self):
        x_list = []
        y_list = []
        
        for x, y in self.data:
            x_list.append(x)
            y_list.append(y)
        
        color = ['r', 'g', 'b', 'k']
        for i, lab in enumerate(self.labels):
            print(i, lab)
            plt.plot(x_list[i], y_list[i], marker = 'o', c = color[lab])

        for i , (x,y) in enumerate(self.centers):
            plt.plot(x,y, marker ='^', c = color[i], ms = 20)
            
        plt.show()

    def animations(self, data, label_set , center_set):
        fig = plt.figure()
        color = ['m','g','b','k','r']
        ims = []
        j = 0
        for label in label_set:
            j += 1
            for i, lab in enumerate(label):
                #print(i)
                plt.plot(data[i][0], data[i][1], marker = 'o', c = color[lab] )
                title = str(j) + ' label'
                plt.title(title)
            plt.show()
            # sleep(0.2)
            
def coh(k):
    print('아직 구현 안됨 ㅎ')
    pass

def div(k, datanum):
    data = load_dataset(datanum,k)
    k = DIV(data,k)
    k.clustering()
    

def load_dataset(n,k):
    dataset = np.array([[1,1],[2,2]])
    num = int(n / k)
    for i in range(k):
        dataset = np.concatenate((dataset , np.random.randn(num , 2) + (i+1)*(i+1)), axis = 0)
    return dataset

def main():
    parser = argparse.ArgumentParser(description = 'This code is written for Algorithm-briefing about Clustering')
    parser.add_argument('--mode', type = str, default = 'div', choices = ['coh','div'],metavar = '["coh", "div"]', help = 'Choose a mode about algorithm and start!')
    parser.add_argument('--k', type = int, default = 2 , choices = [2,3,4,5], metavar = 'Choose a number of Cluster', help = 'What do you want the number of cluster?' )
    parser.add_argument('--datanum', type = int, default = 50, metavar = 'Choose a number of data', help = '데이터 수 입력하라고요!')
    args = parser.parse_args()

    MODE = args.mode
    K = args.k
    datanum = args.datanum

#    print(MODE, K)

    if MODE == 'coh':
        coh(K)
    else:
        div(K, datanum)

if __name__ == "__main__":
    main()