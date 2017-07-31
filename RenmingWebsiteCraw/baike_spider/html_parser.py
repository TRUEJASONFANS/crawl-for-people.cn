#  -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        # personPage\d+.htm
        links = soup.find_all('a', href=re.compile(r'personPage\d+.htm'))
        new_urls = set()
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        links = soup.find_all('a', href=re.compile(r'personProvince\d+.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls   
    def _get_new_data(self, page_url, soup):
        
        res_data = {}
        # if the url match the province url
        if re.match(r'http://ldzl.people.com.cn/dfzlk/front/personProvince\d+\.htm', page_url):
            
            res_data['url'] = page_url
            # 
            city_node = soup.find('div', class_='fr p2j_sheng_right title_2j').find('h1', class_='red')
            res_data['city'] = city_node.get_text()
            
            title_node = soup.find('span', class_="red2")
            res_data['title'] = title_node.get_text()
            
            name_node = soup.find('dd').find('em').find('a')
            if name_node is None:
                return res_data
            res_data['name']  = name_node.get_text()
            return None
        if re.match(r'http://ldzl.people.com.cn/dfzlk/front/personPage\d+.htm', page_url):
            res_data['url'] = page_url
            
            title_node = soup.find('span', class_="red2")
            res_data['title'] = title_node.get_text()
            
            name_node = soup.find('dd').find('em')
            if name_node is not None:
                res_data['name']  = name_node.get_text()
            
            personal_info_nodes = soup.find('dd').find_all('b')
            index = 0
            for node in personal_info_nodes:
                content_key = node.get_text()
                content = node.next_sibling;
                print content_key
                print content
                if index == 0:
                    res_data['sex'] = content
                elif index ==1:
                    res_data['birthday'] = content
                elif index ==2:
                    res_data['hometown'] = content
                elif index ==3:
                    res_data['education'] = content
                index = index + 1
        return res_data 
    
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser' , from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    
    


