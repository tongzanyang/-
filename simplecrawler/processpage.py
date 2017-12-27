from bs4 import BeautifulSoup, SoupStrainer
import requests
from simplecrawler.pagequeue import PageQueue
from simplecrawler.visitedpages import VisitedPages
from simplecrawler.sitemap import SiteMap,URLType
from simplecrawler.root import Root


class ProcessPage():
    STATUS_DONE = "DONE"
    STATUS_OK = "OK"
    STATUS_ERROR = "ERROR"
    STATUS_GOOD = 200
    STATUS_INVALID_URL = "ERROR_URL"
    STATUS_BAD_INDEX = -1
    EMPTY_RETURN = ""
    #
    #remove trailing web addr chars such as # and ?
    #  also delete the last char if it is '/'
    def remove_trailing_web_addr_chars(self, orig_url):
        check_chars = ['#','?']
        for c in check_chars:
            try:
                indx_char = orig_url.index(c)
                orig_url = orig_url[0:indx_char]
            except:
                pass
        if len(orig_url) > 0 :
            if orig_url[-1] == "/":
                orig_url = orig_url[0:-1]
        return orig_url
    #
    # check for valid Web page url which start
    #    with either http ot https
    #  returns the first char after the protocol header or
    #    BAD_INDEX if the the protocol header is not found
    def get_index_start_domain_name(self, orig_url):
        if len(orig_url) == 0 :
            return self.STATUS_BAD_INDEX
        valid_prefix_list = ['http://','https://']
        # valid prefix includes http://, https://
        check_url = orig_url.lower()
        index_pos = self.STATUS_BAD_INDEX
        for valid_pref in valid_prefix_list:
            try:
                index_pos =  check_url.index(valid_pref)
                index_pos += len(valid_pref)
            except:
                pass
        return index_pos

    #
    #  retunrn the domain name or INVALID_URL if domain is not valid
    #   normalize the result by removing "www." if it exists
    #  remove everything after the first forward slash ('/'), if it exists
    #   in the normalized domain name
    #
    def get_domain_name(self, orig_url):
        # normalize by removing leading "www."
        #   convert to lowercase
        leading_www = "www."
        start_indx = self.get_index_start_domain_name(orig_url)
        if start_indx == self.STATUS_BAD_INDEX:
            return self.STATUS_INVALID_URL
        name_domain = orig_url[start_indx:].lower()
        try:
            slash_indx_pos = name_domain.index('/')
        except:
            slash_indx_pos = -1
        if slash_indx_pos > -1 :
            name_domain = name_domain[0:slash_indx_pos]

        if len(name_domain) >= len(leading_www):
            if name_domain[0:len(leading_www)] == leading_www:
                name_domain = name_domain[len(leading_www):]
        return name_domain




    #   vaidateUrl
    #       check length .gt. 0,
    #           if len == 0, return STATUS_ERROR
    #       remove trailing slash
    #       initial check for redirect
    #           if redirect, return STATUS_ERROR
    #       if validated, then return self.STATUS_OK
    #
    def validate_url(self, r, current_url):

        if len(current_url) == 0:
            print(" url invalid " )
            print(" ... skipping")
            return (self.STATUS_ERROR,current_url, )
        #remove trailing slash
        if current_url[-1] == "/":
            current_url = current_url[0:-1]

        bs_obj = BeautifulSoup(r.content,"html.parser")
        html_meta = bs_obj.meta
        if html_meta != None and html_meta.has_attr('content'):
            html_meta_content = html_meta['content']

            ri = html_meta_content.find("url=")
            if ri != -1:
                # url detected in the meta: prob a redirect
                ri += len("url=")
                current_url_len_offset = len(current_url) + ri
                validate_no_redirect = html_meta_content[ri:current_url_len_offset]
                if current_url != validate_no_redirect:
                    print("url redirected:")
                    print(" ... skipping")
                    return (self.STATUS_ERROR, current_url)
        else:
            pass

        return (self.STATUS_OK, current_url)



    def process_image_ref(self, r, current_url):

        soup_obj = BeautifulSoup(r.content, "html.parser")
        tags = soup_obj.findAll('img')
        #print (type(tags))
        image_url_set = set()
        site_map = SiteMap()
        for tag in tags:
            #if 'src' in tag:
            if tag.has_attr('src'):
                image_url = str(tag['src'])
                if image_url not in image_url_set:
                    site_map.add_to_sitemap(current_url, image_url, URLType.IMAGE_LINK)
                    image_url_set.add(image_url)
        return  self.STATUS_OK

    #
    #
    # the process_href processes the next URL from
    #     the page queue
    #
    def process_href(self, r, current_url):
        # use set to eliminate duplicates
        #root = Root()
        root_domain = Root.root_domain
        page_q = PageQueue()
        visited_pages = VisitedPages()
        site_map = SiteMap()
        link_url_set = set(current_url)

        #get all the href URLs
        for link in BeautifulSoup(r.content, "html.parser", parseOnlyThese=SoupStrainer('a')):
            if link.has_attr('href'):
                #process all the hrefs
                link_url = link['href']
                if len(link_url) == 0:
                    # empty
                    link_url = "/"
                # check for urls that start with '/'
                if link_url[0] == '/':
                    try:
                        # special append protocol
                        slash_indx_pos = link_url.index('.')
                        link_url = "http:/" + link_url
                    except:
                        # special url format, append protocol + domain
                        link_url = "http://" + root_domain + link_url
                # check for urls that dont start   http, ot https
                if self.get_index_start_domain_name(link_url) == self.STATUS_BAD_INDEX:
                    link_url = "http://" + root_domain + '/' + link_url
                link_url_with_additional_web_chars = link_url
                link_url = self.remove_trailing_web_addr_chars(link_url)

                if len(link_url) > 0 :
                    if link_url not in link_url_set:
                        link_url_set.add(str(link_url))
                        current_url_domain_name = self.get_domain_name(link_url)
                        if current_url_domain_name == self.STATUS_INVALID_URL:
                            site_map.add_to_sitemap(current_url, link_url, URLType.NOT_INDOMAIN_LINK)
                        elif  current_url_domain_name != root_domain:
                            site_map.add_to_sitemap(current_url, link_url, URLType.NOT_INDOMAIN_LINK)
                        else:
                            # in current domain
                            site_map.add_to_sitemap(current_url, link_url, URLType.INDOMAIN_LINK)
                            # check if previously visited
                            if visited_pages.checkVisitedPagesSet(link_url)  == False :
                                # add to queue

                                page_q.append(link_url_with_additional_web_chars)
                                visited_pages.add(link_url)


        return


    # main Scraper logic
    def scrape(self):
        myobject_q = PageQueue()
        # anymore URLs to process?
        if (myobject_q.is_empty()):
            return self.STATUS_DONE, self.EMPTY_RETURN
        #process the next URL
        url_from_q = myobject_q.pop_left()

        try:
            # get the page
            r = requests.get(url_from_q)
        except requests.exceptions.RequestException as e:
            return self.STATUS_ERROR, url_from_q
        current_url = r.url
        # normalize the URL : remove trailing slash & check for redirection
        stat, current_url = self.validate_url(r, current_url)
        if stat == self.STATUS_ERROR:
            return self.STATUS_ERROR, url_from_q
        # process the page and the normalized url
        self.process_href(r, current_url)
        #
        self.process_image_ref(r, current_url)

        return self.STATUS_OK,url_from_q
