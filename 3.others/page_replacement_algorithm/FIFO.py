from Cache import Cache
from Page import Page

class FIFO(Cache):
    """ init
    self.currsize = 0
    self.maxsize = maxsize
    self.queue = deque()
    self.hits = 0
    self.misses = 0
    """
    def remove(self, idx):
        self.queue.popleft()
        pass

    def push(self, page : Page):
        self.queue.append(page)
        pass

    def update(self, idx, page:Page):
        self.queue.remove(page)
        pass
    pass

if __name__ == "__main__":
    c = FIFO(30)
    c.cache_info()
    pass