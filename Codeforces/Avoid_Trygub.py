import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    a = read(str)
    b = ''.join(sorted(a))
    print(b)
