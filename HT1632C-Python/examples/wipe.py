import time

from ht1632cpy import HT1632C

interface = HT1632C(1, 0)
interface.pwm(15)


print('panel width is ' + repr(interface.width()) +'.')
print('panel height is ' + repr(interface.height()) + '.')

for x in range(0, 32):
  for y in range(0, 32):
    interface.plot(x,y,interface.GREEN)
    print('pixel at x=' + repr(x) + ', y=' + repr(y) + '...')
    interface.sendframe()

interface.clear()
interface.sendframe()
