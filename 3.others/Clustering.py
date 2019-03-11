import numpy as np

class KMeans:
    def __init__(self, k, dim):
        self.k = k
        self.dim = dim

    def update_centers(self, labels, data):
        print(data)
        print(labels)
        for i in range(self.k):
            print(np.mean(data[np.where(labels == i)], axis = 0))
            self.centers[i] = np.mean(data[np.where(labels == i)], axis = 0)

    def nearest(self, x, centers):
        sims = [self.sim(x,c) for c in centers]
        return sims.index(max(sims))

    def sim(self, x, y):
        return np.dot(x,y) / (np.linalg.norm(x)*np.linalg.norm(y))

    # def centers(self):
    #     return self.centers

    def clustering(self, data):
        self.centers = data[np.random.randint(0, len(data), self.k)]
        labels = np.random.choice([0, 1], self.k)
        print('ori:', labels)
        old_labels = [l for l in labels]
        print(self.centers)
        while True:
            labels = np.array([self.nearest(d, self.centers) for d in data])

            if np.all(labels == old_labels):
                break
            else:
                old_labels = np.copy(labels)
                print('change')
                self.update_centers(labels, data)                
        return labels

if __name__ == "__main__":
    cl = KMeans(3,3)
    a = np.array([1,2,3,4,5,8,9,10,11,12])
    label = cl.clustering(a)
    print(label)
