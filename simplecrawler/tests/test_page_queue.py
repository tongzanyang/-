import unittest
#Testing for Queue
from simplecrawler.pagequeue import PageQueue


class PageQueueTest(unittest.TestCase):
    testURL = "wiprodigital.com"
    multipleUrlTestCount = 1000
    def test_queue_should_initially_have_root_url_append(self):
        myobject_q = PageQueue()
        myobject_q.clear()
        myobject_q.append(self.testURL)
        count_url = myobject_q.len()
        self.assertEqual(count_url,1)

    def test_queue_initial_root_url_pop(self):
        myobject_q = PageQueue()
        myobject_q.clear()
        myobject_q.append(self.testURL)
        current_url = myobject_q.pop_left()
        self.assertEqual(current_url,self.testURL)
        count_url = myobject_q.len()
        self.assertEqual(count_url, 0)

    def test_queue_insert_pop_multiple(self):
        myobject_q = PageQueue()
        myobject_q.clear()
        for x in range(0, self.multipleUrlTestCount):
            new_url = self.testURL + repr(x)
            myobject_q.append(new_url)
        for x in range(0, self.multipleUrlTestCount):
            new_url = self.testURL + repr(x)
            current_url = myobject_q.pop_left()
            self.assertEqual(new_url, current_url)
        count_url = myobject_q.len()
        self.assertEqual(count_url, 0)
