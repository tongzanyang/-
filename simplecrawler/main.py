import sys
sys.path.append('..')
from simplecrawler.crawler import Crawler
from simplecrawler.sitemap import SiteMap
from mock import patch

def testrun():
    print("main invoked for testrun")
    testurl_OK = "http://wiprodigital.com"
    #testurl_OK = "http://msnbc.com"
    rOpt = "-r" + testurl_OK
    testargs = ["simplecrawler", rOpt]
    with patch.object(sys, 'argv', testargs):
        run()


def run():
    print("main invoked")

    crawl = Crawler()
    if crawl.crawl() == True:
        # output the sitemap
        siteMap = SiteMap()
        print ("Sitemap has " + str(siteMap.size())  + " entries")
        siteMap.display_sitemap()

if __name__ == "__main__":
    run()
