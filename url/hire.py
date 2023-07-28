# -*- coding: utf-8 -*-
import os
from urllib import request
from fake_useragent import UserAgent
import requests
import re

class Hire(object):
    def __init__(self, url):
        self.url = url
        self.ua = UserAgent()
        self.decode = 'utf-8'
        self.headers = {'User-Agent': self.ua.edge}
        
    def get_html(self):
        #get html txt from website
        req = request.Request(url=self.url, headers=self.headers)
        res = request.urlopen(req)
        html=res.read().decode("utf-8","ignore")
        res= requests.get(self.url,headers=self.headers)
        # set code 
        res.encoding="utf-8"
        # get html text
        html=res.text
        return html
    
    def get_url_file(self, html):
    #     file_addr = "https://www.analog.com/media/en/engineering-tools/design-tools/ad7173-8_filter_model.xlsx"
        result = re.findall(r"[^=\s]*.xlsx\"", html)
        file_suffix = set(result)
        print(type(file_suffix))
        print(file_suffix)
        for key in file_suffix:
            # file_name = re.findall(r"[^/\s]*.xlsx\"", key)
            file_url = "https://www.analog.com/" + eval(key)
            print(file_url)
            file_name = re.findall(r"[^/\s]*.xlsx", file_url)
            print(file_name)
            try:
                r = requests.get(file_url)
            except Exception as e:
                raise("requests Fail!")
            with open(file_name[0], "wb") as fp:
                fp.write(r.content)

if __name__ == '__main__':
    url = "https://www.analog.com/cn/products/ad7173-8.html#product-documentation"
    # url = "chrome-extension://ncpkioolbefiinmbflfglojjabaipegg/web_accessible_resources/status_on.png"
    hire = Hire(url)
    html = hire.get_html()
    # print(html)
    hire.get_url_file(html)    