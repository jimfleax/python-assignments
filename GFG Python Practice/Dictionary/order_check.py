# Order Check
from collections import OrderedDict
def check_order(s, p):
    d = OrderedDict.fromkeys(s)
    ptr = 0
    for k in d:
        if k == p[ptr]: ptr += 1
        if ptr == len(p): return True
    return False
print(check_order('engineers rock', 'er'))
