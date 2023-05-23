import math
import sys


def fun(num):
    list = [a * a for a in range(1, int(math.sqrt(num)) + 1)]
    dp = {}
    ans = least_sqr_num(num, 0, list, dp)
    print(ans)


def least_sqr_num(target, i, list, dp):
    if (target, i) in dp:
        return dp[(target, i)]
    if i >= len(list):
        if target == 0:
            return 0
        else:
            return sys.maxsize
    if target == 0:
        return 0
    if target < 0 or target < list[i]:
        return sys.maxsize

    a = 1 + least_sqr_num(target - list[i], i, list, dp)
    b = least_sqr_num(target, i + 1, list, dp)
    dp[(target, i)] = min(a, b)
    return dp[(target, i)]


def inc(x):
    return x + 1


if __name__ == '__main__':
    data = [1, 2, 3]
    print(list(map(inc, data)))

    fun(26)
