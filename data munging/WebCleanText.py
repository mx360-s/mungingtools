# A very simple step: When we make web scraping the text can contain extra-spaces, new line character and so on. This function delete that.
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
