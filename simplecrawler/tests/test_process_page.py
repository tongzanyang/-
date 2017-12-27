import unittest
from simplecrawler.pagequeue import PageQueue
from simplecrawler.processpage import ProcessPage

#Testing for Queue





class testProcessPage(unittest.TestCase):
    testurl_ok = "http://wiprodigital.com"
    testurl_err = "http://wiprodigitalx.com"

    def test_processurl_url_list_empty(self):
        myobject_q = PageQueue()
        myobject_q.clear()
        build_sitemap = ProcessPage()
        scrape_output, url_name  = build_sitemap.scrape()
        self.assertEqual(scrape_output, ProcessPage.STATUS_DONE)
        print("=======>test_processurl_url_list_empty" + " COMPLETE")

    def test_processurl_url_one_good_element(self):
        myobject_q = PageQueue()
        myobject_q.clear()
        myobject_q.append(self.testurl_ok)
        build_sitemap = ProcessPage()
        scrape_output,url = build_sitemap.scrape()
        self.assertEqual(scrape_output, ProcessPage.STATUS_OK)
        print("=======>test_processurl_url_one_good_element" + " COMPLETE")

    def test_processurl_url_one_bad_element(self):
        myobject_q = PageQueue()
        myobject_q.clear()
        myobject_q.append(self.testurl_err)
        build_sitemap = ProcessPage()
        scrape_output, url_name = build_sitemap.scrape()
        self.assertEqual(scrape_output, ProcessPage.STATUS_ERROR)
        print("=======>test_processurl_url_one_bad_element" + " COMPLETE")




