# Web Scraping #

 - [GetMozService](GetMozService.py)
     - When we make web scraping sometimes need start a webdriver, this function start a Mozilla driver and then install it if is not present. Example of use:
    >
          from bs4 import BeautifulSoup
          from µnging import GetMozService
          #
          url_Base = "https://pagename.com/busqueda/en1/use/"
          driver = GetMozService()
          driver.get(url_Base)
          pageDTA = driver.page_source
          soup = BeautifulSoup(pageDTA, 'lxml')
          print(soup)
    >
