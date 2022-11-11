# µnging tools
# Numeric Tools and Data Dictionary
import pandas as pd
import numpy as np
# String tools
from json import dumps
from yaml import safe_load
from fold_to_ascii import fold
# Date Tools
import datetime

def decimalToBinary(n):
    return ''.join(format(ord(i), '08b') for i in n)
#
# Jaccard Distance
# By David Ochoa
def JaccardDistance(A,B):
    a=set(A.lower())
    b=set(B.lower())
    d = (float(len(a.intersection(b))) / len(a.union(b)))
    return d
#
# Hamming Distance
# By David Ochoa
def HammingDistance(x, y):
    x=x.lower()
    y=y.lower()
    d= float((sum(xi != yi for xi, yi in zip(x, y))+0.00000001))
    return d

# Longest common substring recursion
# Original code by Ryuga

def lcs(i,j,X,Y,count):
    if (i == 0 or j == 0):
        return count
    if (X[i - 1] == Y[j - 1]):
        count = lcs(i - 1, j - 1,X,Y, count + 1)
    count = max(count, max(lcs(i, j - 1,X,Y, 0), lcs(i - 1, j,X,Y, 0)))
    return count

'''
# ==============================================================
    				           	    String tools


inspired by anrie's hack https://stackoverflow.com/a/56592789/14879731
'''
#
# When Make web scraping the data commonly has a title and the data are after ':'
# Consume string and return a dictionary
# No dependecies
def KeyAndValue(a, d):
    b = fold(a).split(d)
    c = dict()
    c[b[0]] = b[1]
    return c

# When Make web scraping the text can contain extra-spaces. This function delete that.
# Consume string and return string
# No dependecies

def ExtraWhite(a):
    a = fold(a)# "Clean" to common ascii
    a = safe_load(a)# load as yaml cleaning linebreaks with some tolerance
    a = str(dumps(a))# Trnasform in "orthodoxe" string object
    return a

# When Make web scraping the text can contain extra-spaces, new line character and other by the way. This function delete that.
# Consume string and return ‘Basic Latin’ Unicode block string
# fold_to_ascii as dependecy

def WebCleanText(a):
    B = ''
    A = ' '
    a = ExtraWhite(a)
    a = a.replace('"',B).replace(',',A)
    a = a.replace('  ',B)
    return a

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
#
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
'''
# ==============================================================
    				Numerical Format Transformations

'''
def Toint8(DataSET,ToEdit):
    for i in ToEdit:
        chng=[]
        for j in DataSET[i]:
            try:
                chng.append(np.int8(j))
            except:
                chng.append(None)
        DataSET[i] = chng
    return DataSET

def Toint32(DataSET,ToEdit):
    for i in ToEdit:
        chng=[]
        for j in DataSET[i]:
            try:
                chng.append(np.int32(j))
            except:
                chng.append(None)
        DataSET[i] = chng
    return DataSET

def Tofloat64(DataSET,ToEdit):
    for i in ToEdit:
        chng=[]
        for j in DataSET[i]:
            try:
                chng.append(np.float64(j))
            except:
                chng.append(None)
        DataSET[i] = chng
    return DataSET

def ToStr(DataSET,ToEdit):
    for i in ToEdit:
        chng=[]
        for j in DataSET[i]:
            try:
                chng.append(str(j))
            except:
                chng.append(None)
        DataSET[i] = chng
    return DataSET
'''
# ==============================================================
    				           Data Dictionary Setup

The idea behind this section is create a Table with a syntesis of
the data propierties, to see the data before start clean and without
make bautifull but useless graphs.

The graphics is logic to make after the data format correction
'''
#
# ==============================================================
#                                        Create a DataDictionary
#
def CreateDataDictionary(Variables,NewColumns):
    Variables.columns = NewColumns.keys()
    DataDictionary = pd.DataFrame()
    for c in Variables.columns:
        DataDictionary[c]=Variables[c].groupby(type).unique()
    #--
    DataDictionary=DataDictionary.T
    DataDictionary.columns=['Values']
    #--
    chng=[]
    chng2=[]
    for i in DataDictionary['Values']:
        chng.append(i.shape[0])
        chng2.append( str(type(i[0])).replace("<class '",'').replace("'>",'') )
    DataDictionary['Disctint']  = chng
    DataDictionary['Type']      = chng2
    DataDictionary['Description']= NewColumns.values()
    print('The number of variables in the raw dataset is:',DataDictionary.shape[0])
    #Memory
    # * The dataset does not contain a numeric index, now i will create one
    NewIndex=list(range(len(DataDictionary)))
    DataDictionary['Variable'] = DataDictionary.index.values
    DataDictionary['Id'] = NewIndex
    #Memory
    #
    DataDictionary.set_index(DataDictionary['Id'], inplace=True)
    DataDictionary.drop(['Id'], axis=1, inplace=True)
    return DataDictionary
#
# ==============================================================
#                                Populate a Measurement Accuracy
#
def CalculateMeasurementAccuracy(Variables,NewColumns):
    DataDictionary=CreateDataDictionary(Variables,NewColumns)
    μ = DataDictionary.Disctint.median()
    n = DataDictionary.shape[0]
    MeasurementAccuracy = []
    for i in range(n):
        MAtemp = (DataDictionary['Disctint'][i] / μ)
        MeasurementAccuracy.append(MAtemp)
    #
    DataDictionary['MeasurementAccuracy'] = MeasurementAccuracy
    DataDictionary= DataDictionary.sort_values(by=['Disctint'], ascending=True)
    #Memory
    #
    return DataDictionary
#
# ==============================================================
#                                                     Clusterize
#
def CreateCluster(Variables,NewColumns):
    DataDictionary=CalculateMeasurementAccuracy(Variables,NewColumns)
    dfr=pd.DataFrame(DataDictionary['MeasurementAccuracy'])
    #
    bins =  np.arange(step=(1),start=0, stop=4)
    Cluster = np.digitize(dfr, bins)
    #
    DataDictionary['Cluster']=Cluster
    DataDictionary.sort_values(by=['MeasurementAccuracy'],inplace=True)
    #Memory
    return DataDictionary
#
# ==============================================================
#                                                          Nulls
#
def CountDictionaryNulls(Variables,NewColumns):
    DataDictionary=CreateCluster(Variables,NewColumns)
    Nulls=Variables.isnull().sum()
    Nulls.sort_index(ascending=False, inplace=True)
    DataDictionary.sort_values(by='Variable',ascending=False, inplace=True)
    DataDictionary['Nulls']=Nulls.values
    return DataDictionary
#
# ==============================================================
#                                Order and Return The Dictionary
#
def GetDataDictionary(Variables,NewColumns):
    DataDictionary=CountDictionaryNulls(Variables,NewColumns)
    DataDictionary.insert(0, 'Variable', DataDictionary.pop('Variable'))
    DataDictionary.insert(1, 'Cluster', DataDictionary.pop('Cluster'))
    DataDictionary.insert(2, 'Disctint', DataDictionary.pop('Disctint'))
    DataDictionary.insert(3, 'Values', DataDictionary.pop('Values'))
    DataDictionary.insert(4, 'Nulls', DataDictionary.pop('Nulls'))
    DataDictionary.insert(4, 'Type', DataDictionary.pop('Type'))
    DataDictionary.pop('MeasurementAccuracy')
    DataDictionary.sort_values(by='Cluster',ascending=False, inplace=True)
    return DataDictionary
