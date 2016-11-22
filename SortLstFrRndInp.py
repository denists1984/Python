a = [] #"hello world and practice makes perfect and hello world again"
b = []
while len(a) < 10:
    a.append(raw_input(':-->'))

for i in a:
    if i not in b:
        b.append(i)

print sorted(b)
