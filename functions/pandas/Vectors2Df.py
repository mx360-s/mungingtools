# In this case convert a vector list to Pandas Data Frame
# ingest a list of lists and a list of column names <- Vector2Df([y,u], c)
# return a pandas dataframe
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
