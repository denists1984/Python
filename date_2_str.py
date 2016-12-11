import datetime

a = datetime.datetime.now()
def to_string(a):
    b = a.strftime('%d %B %Y')
    return b

s = to_string(a)
print s
