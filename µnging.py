# µnging tools
#
# When Make web scraping the data commonly has a title and the data are after ':'
# Consume string and return a dictionary
# No dependecies
def KeyAndValue(a,d):    
    b = a.split(d)
    c=dict()
    c[b[0]]=b[1]
    return c

# When Make web scraping the text can contain extra-spaces. This function delete that.
# Consume string and return string
# No dependecies
def RemoveExtraWhite(a):
    d = a.split()
    b = d.copy()
    for c in range(len(d)):
        if c == 0:
            if d[c] == '': b[c].remove
        else: None
        if d[c-1] != '':
            if d[c] == '': b[c].remove
    e = " ".join(b)
    return e

# When Make web scraping the text can contain extra-spaces, new line character and other by the way. This function delete that.
# Consume string and return string
# No dependecies
def WebCleanText(a):
	B=''
	A=' '
	a.replace(',',A).replace("'",B).replace('  ',A).replace('\t',B).replace('\r',B).replace('\n',B).replace('[',A).replace(']',A)
	a.split(A)
	C=len(a)-1
	D=0
	if a[0]==A:D=1
	else:D=0
	if a[C]==A:E=C-1
	else:E=C
	F=str(a[D:E])
	return F
# pandas
# In this case convert a vector list to Pandas Data Frame
# ingest a list of lists and a list of column names <- Vector2Df([y,u], c)
# pandas as dependency
#
from pandas import DataFrame
# Exceptions
class vectors(Exception):
	def __init__(vectors,error,message='o_0 \n Inconsistency: Diferent Number of Vectors & Column Names'):vectors.error=error;vectors.message=message;super().__init__(vectors.message)
	def __str__(vectors):return f"{vectors.error} -> {vectors.message}"
class rows(Exception):
	def __init__(rows,error,message='0_o \n Diferent Number Of Rows in Vectors'):rows.error=error;rows.message=message;super().__init__(rows.message)
	def __str__(rows):return f"{rows.error} -> {rows.message}"
# vector list to Pandas Data Frame
def Vectors2Df(b=None, c=None):
    dic = {}
    if len(b) != len(c):  raise vectors(Exception)
    else:
        try:
            for d in range(len(c)):
                dic[c[d]] = b[d]
            df = DataFrame(data=dic)
            return df
        except: raise rows(Exception)

y = ['a','b','c']
u = ['d','e','f']
c = ['g',2]
Vectors2Df([y,u], c)
Vectors2Df([u], str(c[0]) )
# Web Scraping
# Start a web driver service with mozilla
# None to ingest, return a web driver service with mozilla
# Selenium and webdriver as dependencies
#
# Exceptions
class NonInstall(Exception):
	def __init__(NonInstall,error,message="o_0 \n Driver not present, and can't install"):NonInstall.error=error;NonInstall.message=message;super().__init__(NonInstall.message)
	def __str__(NonInstall):return f"{NonInstall.error} -> {NonInstall.message}"
#
def GetMozService():
    # instalamos el Gecko Driver solo la primera vez es necessario
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    options = Options()
    options.add_argument( '--disable-blink-features=AutomationControlled' )
    options.add_argument('--single-process')
    options.add_argument("disable-infobars")
    options.set_preference('useAutomationExtension', False)# Marioneta
    options.set_preference("dom.webdriver.enabled", True)# Shadowdom
    try:
        try:
            driver = webdriver.Firefox(options=options)            
        except:
            print('trantando de instalar webdriver')
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), executable_path='geckodriver.exe')
    except: raise NonInstall(Exception)
    return driver
