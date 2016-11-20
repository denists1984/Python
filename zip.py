re = [1, 2 ,3]
be = ['a', 'b', 'c']

def list_2tuple(re, be):
    s = zip(re, be)
    return s

fe = list_2tuple(re, be)
print fe
