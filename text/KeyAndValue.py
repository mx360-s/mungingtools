# David Ochoa 2022 MIT lic
# When Make web scraping the data commonly has a title and the data are after ':'
# Consume string and return a dictionary
# No dependecies
def KeyAndValue(a,d):    
    b = a.split(d)
    c=dict()
    c[b[0]]=b[1]
    return c
