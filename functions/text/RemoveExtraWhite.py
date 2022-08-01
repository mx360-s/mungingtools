# David Ochoa 2022 MIT lic
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
