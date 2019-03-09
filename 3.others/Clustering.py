import numpy as np

class KMeans:
    def __init__(self, k, dim):
        self.k = k
        self.dim = dim

    def clustering(self, data):
        self.centers = data[np.randon.randint(0, len(data), self.k)]
        labels = np.random.choice([0, 1], self.k)
        old_labels = [l for l in labels]

        while True:
            labels = np.array([self.nearest(d, self.centers) for d in data])

            if np.all(labels == old_labels):
                break
            else:
                old_labels = np.copy(labels)
                self.update_centers(labesl, data)