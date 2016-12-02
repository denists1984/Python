
iter = 5
num = 9

import random
def nchoices(iter, num):
    my_list = []
    for i in range(num):
        my_list.append(random.choice(iter))
    return my_list

a = nchoices(iter, num)
print a
