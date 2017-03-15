import math
import random

import main


def test():
    print("Function Test")
    for i in range(0, 100000):
        h = random.randint(0, 12)
        m = random.randint(0, 59)
        rad = main.time2rad(h, m)
        t = main.rad2time(rad[0])
        print("Test case %s : %s : %s -> %s, %s -> %s : %s ? %s" % (
            i + 1, h, m, math.degrees(rad[0]), math.degrees(rad[1]), t[0], t[1], (h, m) == t))
        assert (h, m) == t

    print("\nCircularity Test")
    for i in range(0, 100000):
        h = random.randint(0, 12)
        m = random.randint(1, 59)
        _, rad = main.time2rad(h, m)
        count = 0
        print("Test case %s : " % (i + 1))
        while not ((h, m) == (4, 48) or h == 0):
            h, m = main.rad2time(rad)
            print('%s:%s' % (h, m))
            _, rad = main.time2rad(h, m)
            count += 1
            if count > 10000:
                print("BOOM!")
                assert False

    print("Test Success!")


if __name__ == '__main__':
    test()
