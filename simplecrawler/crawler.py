from simplecrawler.pagequeue import PageQueue
from simplecrawler.processpage import ProcessPage
from simplecrawler.visitedpages import VisitedPages
from simplecrawler.sitemap import SiteMap
from simplecrawler.root import Root
import sys
import getopt

def usage():
    print ("\nThis is the usage function\n")
    print ('Usage: '+sys.argv[0]+' -r <root url> ')


class Crawler:

    def crawl(self):
        argv = sys.argv[1:]
        try:
            opts, args = getopt.getopt(argv, "r:", ["root"])
        except getopt.GetoptError:
            usage()
            return False

        if len(opts) == 0 :
            usage()
            return False

        root_site = ""
        #root = Root()
        for current_argument, current_value in opts:
            if current_argument in ("-r", "--root"):

                root_site = current_value
                Root.root_url = root_site
                validator = ProcessPage()
                # rootDomain will be the root domain all the urls will be compared against
                root_domain   =  validator.get_domain_name(root_site)
                if root_domain == ProcessPage.STATUS_INVALID_URL:
                    print("Error processing url:[" + root_site + "]")
                    return False
                # root domain is OK
                Root.root_domain   =root_domain
                print("processing site at:" + root_site + ", for Domain:" + root_domain)

        # init data structs
        site_map = SiteMap()
        site_map.clear()
        visited_pages = VisitedPages()
        visited_pages.clear()
        q = PageQueue()
        q.clear()
        # seed the Q with the root page
        q.append(root_site)
        visited_pages.add(root_site)
        # processPage reads pages from the Q
        processor = ProcessPage()
        # run as long as there are pages in the Q
        while True :
            ret_val,url_name = processor.scrape()

            if ret_val == ProcessPage.STATUS_DONE:
                print("Completed creating sitemap for " + Root.root_url)
                break
            elif ret_val != ProcessPage.STATUS_OK:
                # there was an error, print it out but keep going
                print ("Error processing URL: " + url_name)
            else:
                print("Scraped page : " + url_name)
        # done processing the Q, now output the sitemap
        return True