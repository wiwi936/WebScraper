"""
Scraper
"""

class Scraper():
    """Scraper"""

    def __init__(self):
        self._searchers = []
        self._actions = []
        pass
    
    def addSearcher(self, searcher):
        """Add searcher"""
        self._searchers.append(searcher)
        
    def addAction(self, action):
        """Add actions"""
        self._actions.append(action)

    def __do(self, page_url, page_content):
        """performs each searcher and action"""

    def scrap(self, pages):
        """Scrap all pages in dictionary pages {page_url, page_content}"""
        result = []
        for page_url, page_content in pages.items():
            for searcher in self._searchers: 
                searcher.do(page_url, page_content, result)
        for action in self._actions: 
            action.do(result)
