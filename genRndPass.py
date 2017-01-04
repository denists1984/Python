import re
from random import choice
from string import digits, ascii_lowercase, ascii_uppercase


Pass = "simplepass"


while True:
    if re.search(r'\d\w?', Pass):
        print ''
        print "This is the pass New", Pass
        break
    else:
        print "Generated Pass '{}' not matching the requirements. Skipping ".format(Pass)
        Pass = "".join(([choice(digits + ascii_lowercase + ascii_uppercase) for i in range(8)]))
