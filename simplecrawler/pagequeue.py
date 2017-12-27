from collections import deque

#Page Queue hold the url of the pages that will be processed
#     the Queue is maintain in a global python deque object
class PageQueue:
    page_queue = deque()
    def __init__(self):
         pass

    def append(self, url):
        self.page_queue.append(url)

    def len(self):
        return len(self.page_queue)

    def pop_left(self):
        return self.page_queue.popleft()

    def clear(self):
        self.page_queue.clear()

    def is_empty(self):
        if len(self.page_queue) == 0 :
            return True
        else:
            return False



