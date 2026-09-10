import sys
from collections import Counter, defaultdict, deque, namedtuple
import heapq, bisect, string
from math import gcd, lcm, sqrt, ceil, floor, factorial, comb, perm, log2
from itertools import permutations, combinations, product, accumulate, groupby
from functools import lru_cache, reduce


for t in range(int(input())):

    # n, k = map(int, input().split())
    n = int(input())
    
    a = list(map(int, input().split()))

    if a[0] == a[-1] == 0:
        print(0)
        continue

    cnt = a.count(0)

    if cnt >= 2:
        if a[0] == 0 or a[-1] == 0:
            print(1)
            continue
        else:
            print(2)
            continue
    else:
        print(-1)