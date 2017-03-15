import math

tau = math.pi * 2


def time2rad(hour, minute):
    return (tau * (hour / 12)) + ((tau / 12) * (minute / 60)), tau * (minute / 60)


def rad2time(rad):
    h = int(rad / (tau / 12))
    m = round((rad % (tau / 12) / (tau / 12)) * 60)
    return h, m


def main():
    ih, im = map(int, input().split(':'))
    _, rad = time2rad(ih, im)
    while True:
        h, m = rad2time(rad)
        print('%s:%s\n' % (h, m))
        _, rad = time2rad(h, m)
        if h == 0:
            break
        if input() == 'q':
            break


if __name__ == '__main__':
    main()
