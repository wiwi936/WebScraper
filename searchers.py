"""
Searchers
"""

import re
import utils

class Base():
    """
    Searchers abstract class
    """
    def do(self, page, page_content, result):
        raise NotImplementedError("Must implement this")

class FindPage(Base):
    """
    Add to results the page name
    Example:
    searchers.FindPage()
    """
    def do(self, page, page_content, result):
        result.append(page)

class FindImages(Base):
    """
    Find images on tag img
    Example:
    searchers.FindImages()
    """
    def do(self, page, page_content, result):
        for tag in page_content.findAll('img'):
            result.append(tag.get('src'))

class FindLink(Base):
    """
    Find files with extension self._extension on <a> tags
    Example:
    searchers.FindLink()
    searchers.FindLink(".pdf")
    """
    def __init__(self, extension):
        self._extension = extension
        
    def do(self, page, page_content, result):
        for tag in page_content.findAll('a', href=True):
            if tag.get('href').endswith(self._extension):
                result.append(tag.get('href'))

class FindTags(Base):
    """
    Find tags self._tags [of class self._class]
    Example:
    searchers.FindTags(['a', 'div']),
    searchers.FindTags(['h4', 'div'], "genre")
    """
    def __init__(self, tags, clss = None):
        self._tags = tags
        self._class = clss
        
    def do(self, page, page_content, result):
        founds = page_content.find_all(self._tags, attrs={'class':self._class}) if self._class else page_content.find_all(self._tags)
        for found in founds:
            result.append(utils.clean_data(found.contents[0]))
    
class FindRegularExpression(Base):
    """
    Find using regular expression self._re
    Example:
    searchers.FindRegularExpression(r'<title.*?>(.+?)</title>')
    """
    def __init__(self, re):
        self._re = re
        
    def do(self, page, page_content, result):        
        founds = re.findall(self._re, str(page_content))
        for found in founds:
            result.append(utils.clean_data(found))
