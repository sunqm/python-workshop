## both ends

import collections
import threading
import time

candle = collections.deque(range(20))

print("deque", candle)
def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
            print('{:>8} done'.format(direction))
    return
left = threading.Thread(target=burn,
    args=('Left', candle.popleft))
right = threading.Thread(target=burn,
    args=('Right', candle.pop))

left.start()
right.start()

## canc check without join
left.join()
right.join()