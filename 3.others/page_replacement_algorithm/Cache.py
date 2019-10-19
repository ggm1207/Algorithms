from Page import Page
from collections import deque

class Cache(object):
    """Base Cache"""
    def __init__(self, maxsize):
        self.currsize = 0
        self.maxsize = maxsize
        self.queue = deque()
        self.hits = 0
        self.misses = 0

    def cache_info(self):
        print('CacheInfo(hits=%d, misses=%d, maxsize=%d, currsize=%d)'\
        %(self.hits, self.misses, self.maxsize, self.currsize))

    def inspector(self, page : Page):
        """if page in queue plus hits and return idx else plus misses return -1
        Args:
            page : instance of Page class from ./Page.py
        Returns:
            idx : returns page idx if page in queue else returns -1 
        """
        isInQueue, cur_page = False, page.get_pagenum()
        for idx, p in enumerate(self.queue):
            if (p.get_pagenum() == cur_page):
                isInQueue = True
                break
        
        if isInQueue:
            self.hits += 1
            return idx
        else:
            self.misses += 1
            return -1

    def isFull(self):
        return self.currsize == self.maxsize

    def remove(self):
        """delete old page according to policies of each method"""
        pass

    def push(self, page : Page):
        """push the new page"""
        pass

    def update(self, idx, page:Page):
        """update the old page to new page"""
        pass

    def caches(self, page : Page):
        idx = self.inspector(page)
        idx = idx if idx != -1 else False
        if self.isFull():
            if idx: # update and swap
                self.update(idx, page)
            else: # remove and push
                self.remove()
                self.push(page)
            return   
        if idx: # update and swap
            self.update(idx, page)
        else: # push
            self.push(page)

        
if __name__ == "__main__":
    c = Cache(30)
    c.cache_info()