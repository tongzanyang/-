import unittest
from simplecrawler.visitedpages import VisitedPages



class VisitedPagesTest(unittest.TestCase):
    page_test_one = "wiprodigital.com/index.html"
    page_test_two = "wiprodigital.com/random_page"

    def test_visited_page_confirm_not_visited(self):
        visited_page_set = VisitedPages()
        visited_page_set.clear()
        self.assertEqual(visited_page_set.checkVisitedPagesSet(self.page_test_one), False)

    def test_visited_page_confirm_visited_true(self):
        visited_page_set = VisitedPages()
        visited_page_set.clear()
        visited_page_set.add(self.page_test_one)
        retVal = visited_page_set.checkVisitedPagesSet(self.page_test_one)
        self.assertEqual(retVal,True)

    def test_visited_page_confirm_visited_false(self):
        visited_page_set = VisitedPages()
        visited_page_set.clear()
        visited_page_set.add(self.page_test_one)
        retVal = visited_page_set.checkVisitedPagesSet(self.page_test_two)
        self.assertEqual(retVal, False)