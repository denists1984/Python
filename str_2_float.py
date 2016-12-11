a = []
res = "temp=53.7'C"

maxTemp = 50

for i in res:
    try:
        a.append(int(i))
    except ValueError:
        pass
a.insert(2, '.')


b = float(''.join(str(x) for x in a))

#if maxTemp >= 'b -= 5':
print b
print type(b)
