# &mu;nging
Yet another list of small tools in python, you can use the functions or the pseudo-libray; is composed by some parts:

## Text munging ##

A list of very simple steps in the Text Muging:
 - [RemoveExtraWhite](https://github.com/devicemxl/-mu-Munging/blob/raiz/text/RemoveExtraWhite.py)
    - When we make web scraping the text can contain extra-spaces. This function delete that.
 - [WebCleanText](https://github.com/devicemxl/-mu-Munging/blob/raiz/text/WebCleanText.py)
    - When we make web scraping the text can contain extra-spaces, new line character and so on. This function delete that.
 - [KeyAndValue](https://github.com/devicemxl/-mu-Munging/blob/raiz/text/WebCleanText.py)
   - When Make web scraping the data commonly has a title and the data are after ':' or other simbol, this split in key and data

## Pandas Shortcuts ##

A list of very simple shortcuts for pandas work:
 - [Vectors2Df](https://github.com/devicemxl/-mu-Munging/blob/raiz/pandas/Vectors2Df.py)
    - In this case convert a vector list to Pandas Data Frame, ingest a list of lists and a list of column names <- Vector2Df([y,u], c), return a pandas dataframe

## Web Scraping ##

 - [GetMozService](https://github.com/devicemxl/-mu-nging/blob/raiz/Web%20Scraping/GetMozService.py)
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
