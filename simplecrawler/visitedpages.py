

class VisitedPages():
    visited_pages_set =  set()

    def add(self,page):
        self.visited_pages_set.add(page)

    def clear(self):
        self.visited_pages_set.clear()

    def checkVisitedPagesSet(self,page):
        if page in self.visited_pages_set:
            return True
        else:
            return False