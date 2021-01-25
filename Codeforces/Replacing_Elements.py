import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n, d = readList()
    A = readList()
    A.sort()
    ans = 'NO'
    if A[-1] > d:
        if A[0] + A[1] <= d:
            ans = 'YES'
    else:
        ans = 'YES'

    print(ans)
