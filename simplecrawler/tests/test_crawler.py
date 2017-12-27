import unittest
import sys
from simplecrawler.pagequeue import PageQueue
from simplecrawler.crawler import Crawler
from mock import patch




class testCrawler(unittest.TestCase):
    testurl_OK = "http://wiprodigital.com"
    #testurl_OK = "http://cnn.com"
    #testurl_OK = "http://google.com"
    testurl_NOT_OK = "wiprodigital.com"
    test_BadURL = ""

    def test_crawler_main_loop(self):
        print(sys.path)
        r_opt = "-r" + self.testurl_OK
        testargs = ["simplecrawler",r_opt]
        with patch.object(sys, 'argv', testargs):
            loop = Crawler()
            result = loop.crawl()
            self.assertEqual(result, True)
        myobject_q = PageQueue()
        q_is_empty = myobject_q.is_empty()
        self.assertEqual(q_is_empty, True)
        print("=======>test_crawler_main_loop" + " COMPLETE")

    def test_crawler_main_loop_bad_parm(self):
        print(sys.path)
        testargs = ["simplecrawler", "-d", self.testurl_OK]
        with patch.object(sys, 'argv', testargs):
            loop = Crawler()
            result = loop.crawl()
            self.assertEqual(result, False)
        print("=======>test_crawler_main_loop_bad_parm" + " COMPLETE")

    def test_crawler_main_loop_bad_url(self):
        #print(sys.path)
        testargs = ["simplecrawler", "-r", self.test_BadURL]
        with patch.object(sys, 'argv', testargs):
            loop = Crawler()
            result = loop.crawl()
            self.assertEqual(result, False)
        print("=======>test_crawler_main_loop_bad_url" + " COMPLETE")

    def test_crawler_main_loop_invalid_url(self):
        print(sys.path)
        testargs = ["simplecrawler", "-r", self.testurl_NOT_OK]
        with patch.object(sys, 'argv', testargs):
            loop = Crawler()
            result = loop.crawl()
            self.assertEqual(result, False)
        print("=======>test_crawler_main_loop_invalid_url" + " COMPLETE")