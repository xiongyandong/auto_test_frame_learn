

# tel = '13654541214'
# a = tel.find('6')
# print(a)

import datetime
import time

t1 = time.time()

time.sleep(2.5)
t2 = time.time()
t = t2-t1
print('{:.2f}'.format(t))
print(format(t, '.2f'))