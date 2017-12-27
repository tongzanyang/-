from collections import defaultdict


from enum import Enum

class URLType(Enum):
    INDOMAIN_LINK = 1
    NOT_INDOMAIN_LINK = 2
    IMAGE_LINK = 3


class SiteMap():
    site_map =  defaultdict(list)

    def add_to_sitemap(self, page, link, type):
        pair = (link,type)
        self.site_map[page].append(pair)

    def clear(self):
        self.site_map.clear()

    def get_sitemap_In_domain_links(self, page):
        return_list = []
        for pair in self.site_map[page]:
            link, type = pair
            if type == URLType.INDOMAIN_LINK:
                return_list.append(link)
        return return_list

    def size(self):
        return len(self.site_map)

    def get_sitemap_not_In_domain_links(self, page):
        return_list = []
        for pair in self.site_map[page]:
            link, type = pair
            if type == URLType.NOT_INDOMAIN_LINK:
                return_list.append(link)
        return return_list

    def get_sitemap_image_links(self, page):
        return_list = []
        for pair in self.site_map[page]:
            link, type = pair
            if type == URLType.IMAGE_LINK:
                return_list.append(link)
        return return_list

    def display_sitemap(self):
        print("\nDisplay Sitemap")
        for page in self.site_map:
            print ("\nPage Links for Page: " + page)
            print("+++++++  Links in the same domain     ++++++")
            for pair in self.site_map[page]:
                link, type = pair
                if  type == URLType.INDOMAIN_LINK:
                    print ("          " + link )
            print("+++++++  Links NOT in the same domain ++++++")
            for pair in self.site_map[page]:
                link, type = pair
                if type == URLType.NOT_INDOMAIN_LINK:
                    print("          " + link)

            print("+++++++  Image Links                  ++++++")
            for pair in self.site_map[page]:
                link, type = pair
                if type == URLType.IMAGE_LINK:
                    print("          " + link)
