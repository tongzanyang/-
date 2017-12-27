import unittest

from simplecrawler.sitemap import SiteMap
from simplecrawler.sitemap import URLType


class SiteMapTest(unittest.TestCase):
    page = "wiprodigital.com/index.html"
    link = "wiprodigital.com/random_page"

    def sitemap_append_INDOMAIN_LINK(self):
        site_map = SiteMap()
        site_map.clear()
        linkType = URLType.INDOMAIN_LINK
        site_map.add_to_sitemap(self.page, self.link, linkType)
        site_links = site_map.get_sitemap_In_domain_links(self.page)
        size_of_list = len(site_links)
        self.assertEqual(size_of_list,1)

    def sitemap_append_NOT_INDOMAIN_LINK(self):
        site_map = SiteMap()
        site_map.clear()
        link_type = URLType.NOT_INDOMAIN_LINK
        site_map.add_to_sitemap(self.page, self.link, link_type)
        site_links = site_map.get_sitemap_not_In_domain_links(self.page)
        size_of_list = len(site_links)
        self.assertEqual(size_of_list, 1)

    def sitemap_append_IMAGE_LINK(self):
        site_map = SiteMap()
        site_map.clear()
        link_type = URLType.IMAGE_LINK
        site_map.add_to_sitemap(self.page, self.link, link_type)
        site_links = site_map.get_sitemap_image_links(self.page)
        size_of_list = len(site_links)
        self.assertEqual(size_of_list, 1)


    def sitemap_append_INDOMAIN_LINK_Error(self):

        site_map = SiteMap()
        site_map.clear()
        link_type = URLType.INDOMAIN_LINK
        site_map.add_to_sitemap(self.page, self.link, link_type)
        site_links = site_map.get_sitemap_image_links(self.page)
        size_of_list = len(site_links)
        self.assertNotEqual(size_of_list, 1)

    def sitemap_append_NOT_INDOMAIN_LINK_Error(self):
        site_map = SiteMap()
        site_map.clear()
        link_type = URLType.NOT_INDOMAIN_LINK
        site_map.add_to_sitemap(self.page, self.link, link_type)
        site_links = site_map.get_sitemap_In_domain_links(self.page)
        size_of_list = len(site_links)
        self.assertNotEqual(size_of_list, 1)

    def sitemap_append_IMAGE_LINK_Error(self):
        site_map = SiteMap()
        site_map.clear()
        link_type = URLType.IMAGE_LINK
        site_map.add_to_sitemap(self.page, self.link, link_type)
        site_links = site_map.get_sitemap_not_In_domain_links(self.page)
        size_of_list = len(site_links)
        self.assertNotEqual(size_of_list, 1)

    #######

    def test_three_types_of_URLS_same(self):
        self.sitemap_append_INDOMAIN_LINK()
        self.sitemap_append_NOT_INDOMAIN_LINK()
        self.sitemap_append_IMAGE_LINK()

    def test_three_types_of_URLS_not_same(self):
        self.sitemap_append_INDOMAIN_LINK_Error()
        self.sitemap_append_NOT_INDOMAIN_LINK_Error()
        self.sitemap_append_IMAGE_LINK_Error()


    def test_add_multiple_records(self):
        base_domain1 = "wiprodigital.com"
        base_domain2 = "wipro.com"
        site_map = SiteMap()
        site_map.clear()
        link_types_1 = [0,0,0]
        link_types_2 = [0,0,0]
        for i in range(1000):

            link = base_domain1 + "/" "page_" + str(i)
            link_type = i % 3
            link_types_1[link_type] += 1
            if link_type == 0:
                link_type = URLType.INDOMAIN_LINK
            elif link_type == 1:
                link_type = URLType.NOT_INDOMAIN_LINK
            else:
                link_type = URLType.IMAGE_LINK
            site_map.add_to_sitemap(base_domain1, link, link_type)


        prime_num = 863
        for i in range(prime_num):

            link = base_domain2 + "/" "page_" + str(i)
            link_type = i % 3
            link_types_2[link_type] += 1
            if link_type == 0:
                link_type = URLType.INDOMAIN_LINK
            elif link_type == 1:
                link_type = URLType.NOT_INDOMAIN_LINK
            else:
                link_type = URLType.IMAGE_LINK
            site_map.add_to_sitemap(base_domain2, link, link_type)
        #
        site_links = site_map.get_sitemap_In_domain_links(base_domain1)
        self.assertEqual(len(site_links),link_types_1[URLType.INDOMAIN_LINK._value_ - 1])
        #
        site_links = site_map.get_sitemap_not_In_domain_links(base_domain1)
        self.assertEqual(len(site_links), link_types_1[URLType.NOT_INDOMAIN_LINK._value_ - 1])
        #
        site_links = site_map.get_sitemap_image_links(base_domain1)
        self.assertEqual(len(site_links), link_types_1[URLType.IMAGE_LINK._value_ - 1])
        ##
        site_links = site_map.get_sitemap_In_domain_links(base_domain2)
        self.assertEqual(len(site_links), link_types_2[URLType.INDOMAIN_LINK._value_ - 1])
        #
        site_links = site_map.get_sitemap_not_In_domain_links(base_domain2)
        self.assertEqual(len(site_links), link_types_2[URLType.NOT_INDOMAIN_LINK._value_ - 1])
        #
        site_links = site_map.get_sitemap_image_links(base_domain2)
        self.assertEqual(len(site_links), link_types_2[URLType.IMAGE_LINK._value_ - 1])