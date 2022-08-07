# &mu;nging
Yet another list of small tools in python, you can use the functions or the pseudo-libray; this is a small work in progress and is composed by some parts:

## Text munging ##

A list of very simple steps in the Text Muging:
 - **RemoveExtraWhite( *string* )**
    - When we make web scraping the text can contain extra-spaces at start and end, new line character and so on. This function delete that.
 - **WebCleanText( *string* )**
    - When we make web scraping the text can contain extra-spaces in the middle, commas and so on. This function delete that.
 - **KeyAndValue( *string*, *symbol string* )**
   - When Make web scraping the data commonly has a title and the data are after ':' or other simbol, this split in key and data

## Pandas Shortcuts ##

A list of very simple shortcuts for pandas work:
 - **Vectors2Df( *list of vectors*, *list of column names* )**
    - In this case convert a vector list to Pandas Data Frame, ingest a list of lists and a list of column names <- Vector2Df([y,u], c), return a pandas dataframe. Example of use:
    
    >    
         y = ['a','b','c']	
         u = ['d','e','f']	
         c = ['g',2]	
         Vectors2Df([y,u], c)	
         
         Vectors2Df([u], str(c[0]) )
    >
    
## Web Scraping ##

 - **GetMozService()**
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
