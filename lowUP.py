var = "Treehouse"

def func(var):
    a = len(var)/2
    low = var[0:a]
    high = var[a:]
    return low.lower() + high.upper()

a = func(var)
print a
