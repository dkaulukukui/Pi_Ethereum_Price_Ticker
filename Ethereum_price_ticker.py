import time
import feedparser
import requests

from ht1632cpy import HT1632C

def scroll_message(msg, color, bg):
    msg_length = len(msg) * interface.fontwidth(interface.font6x8)

    start = interface.width()
    end = -msg_length - 1

    for x in xrange(start, end, -1):
        interface.clear()
        interface.box(0, 0, interface.width(), interface.height(), bg)
        interface.putstr(x, 1, msg, interface.font6x8, color, bg)
        interface.sendframe()
        time.sleep(1/30.0)


# Example scrolls the message across the screen in different colors.
interface = HT1632C(1, 0)
interface.pwm(15)

old_price =0

var = 1

while var == 1:

  recent_price = float(requests.get('https://api.coinbase.com/v2/prices/ETH-USD/sell').json()['data']['amount'])
  
  string1 = ' Eth ' + repr(recent_price) + ' '
 
  if(recent_price > old_price):
    final_string = chr(30) + string1
  elif(recent_price == old_price):
    final_string = string1
  else:
    final_string = chr(31) + string1

  scroll_message(final_string,1,0)
  
  old_price = recent_price

interface.clear()
interface.sendframe()
