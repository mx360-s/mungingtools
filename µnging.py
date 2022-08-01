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
