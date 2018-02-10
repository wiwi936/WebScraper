#!/usr/bin/env python3

#        ██████╗        ██████╗       
#       ██╔═══██╗      ██╔═══██╗      
# █████╗██║   ██║█████╗██║   ██║█████╗
# ╚════╝██║   ██║╚════╝██║   ██║╚════╝
#       ╚██████╔╝      ╚██████╔╝      
#        ╚═════╝        ╚═════╝       

import searchers, actions, crawler, scraper

if __name__ == "__main__":

    url =  "https://pplware.sapo.pt/"
    
    pages = [ ]

    my_crawler = crawler.Crawler(url, pages)
    my_crawler.deep = 0
    my_crawler.progress_bar = False

    my_crawler.crawl()

    my_scraper = scraper.Scraper()

    my_scraper.addSearcher( searchers.FindImages() )
    #my_scraper.addFinder( searchers.FindLink("pdf") )
    #my_scraper.addFinder( searchers.FindPage() )
    #my_scraper.addFinder( searchers.FindTags(["h4", ], "genre") )
    #my_scraper.addFinder( searchers.FindRegularExpression(r'<title.*?>(.+?)</title>') )
    
    my_scraper.addAction( actions.JoinURL(url) )
    my_scraper.addAction( actions.ExportConsole() )
    #my_scraper.addAction( actions.ExportCSV("downloads") )
    #my_scraper.addAction( actions.Blank() )
    #my_scraper.addAction( actions.GetCount() )
    my_scraper.addAction( actions.Download("downloads") )
    
    my_scraper.scrap( my_crawler.get_pages() )

    print("Done!")
