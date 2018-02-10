"""
Crawler
"""

import os
import urllib
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from urllib.request import urlretrieve

import searchers
import utils

class Crawler():

    def __init__(self, url, pages):        
        self.__url = url
        self.__pages = pages
        self.__page_content = {}
        self.__progress_bar = False
        self.__deep = 0

    @property
    def deep(self):
        return self.__deep

    @deep.setter
    def deep(self, value):
        self.__deep = value

    @property
    def progress_bar(self):
        return self.__progress_bar

    @progress_bar.setter
    def progress_bar(self, value):
        self.__progress_bar = value

    def crawl(self):
        if not self.__pages: 
            self.__pages.append(self.__url)
        else:
            for i in range(len(self.__pages)):
                self.__pages[i] = urllib.parse.urljoin(self.__url, self.__pages[i])   
                     
        if self.__progress_bar:
            print("Crawler: [" , end="")
        for page in self.__pages:
            self.__crawl(page, 0)   
        if self.__progress_bar:
            print("]")   

    def get_pages(self):
        return self.__page_content

    def __crawl(self, page, level):

        if page not in self.__page_content:
            
            self.read(page)
            
            if self.__progress_bar:
                print(".", end="")

            if level < self.__deep:
                result = []
                searchers.FindLink("").do(page, self.__page_content[page], result)
                for link in result:                    
                    new_page = link if utils.is_valid_url(link) else urllib.parse.urljoin(self.__url, link)
                    self.__crawl(new_page, level + 1)                         
        
    def read(self, page):
        try:
            response = requests.get(page, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'})
            if response.status_code == 200:
                self.__page_content[page] = BeautifulSoup(response.content, "html.parser")                
            else: 
                print("Exited with status code: {}", response.status_code)
        except Exception as e: 
            print(e)
