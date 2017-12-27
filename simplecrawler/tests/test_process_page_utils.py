import unittest
from simplecrawler.processpage import ProcessPage

class testProcessPageUtils(unittest.TestCase):
    def test_webpage_url_remove_trailng_chars(self):
        test_urls = [("http://www.wiprodigital.com", "http://www.wiprodigital.com"),
                    ("http://www.wiprodigital.com/index.html#test_pound", "http://www.wiprodigital.com/index.html"),
                    ("http://www.wiprodigital.com/index.html?test_question", "http://www.wiprodigital.com/index.html"),
                    ("http://www.wiprodigital.com/first_page#test_pound", "http://www.wiprodigital.com/first_page"),
                    ("http://www.wiprodigital.com/first_page/second_page?test_quest",
                                "http://www.wiprodigital.com/first_page/second_page")
                    ]
        process_page = ProcessPage()
        for original,modified in test_urls:
            ret_str = process_page.remove_trailing_web_addr_chars(original)
            self.assertEqual(ret_str,modified)


    def test_url_in_same_domain(self):
        test_urls = [("http://www.wiprodigital.com", "wiprodigital.com"),
                    ("https://www.wiprodigital.com", "wiprodigital.com"),
                    ("http://wiprodigital.com/address1/", "wiprodigital.com"),
                    ("https://www.wiProdigital.com/address1/address2", "wiprodigital.com"),
                    ("http://www.wiProdigital.com/addr1/addr2/adddress3/moredata_here", "wiprodigital.com")]
        process_page = ProcessPage()
        for original,derived_domain in test_urls:
            ret_str = process_page.get_domain_name(original)
            self.assertEqual(ret_str,derived_domain)


    def test_url_not_in_same_domain(self):
        testUrls = [("https://help.wiprodigital.com", "wiprodigital.com"),
                    ("http://www.wiprodigital.info", "wiprodigital.com"),
                    ("http://wipro.com/address1/", "wiprodigital.com"),
                    ("https://wiProdigital.edu/address1/address2", "wiprodigital.com"),
                    ("http://support.wiProdigital.com/addr1/addr2/adddress3/moredata_here", "wiprodigital.com")]
        process_page = ProcessPage()
        for original,derived_domain in testUrls:
            retStr = process_page.get_domain_name(original)
            self.assertNotEqual(retStr,derived_domain)