
from collections import Counter

for t in range(int(input())):

    # n, m = map(int, input().split())
    n = int(input())
    
    # a = list(map(int, input().split()))

    a = input()
    b = input()

    odd1 = Counter()
    odd2 = Counter()

    eve1 = Counter()
    eve2 = Counter()

    for i in range(n):
        if i % 2 == 0:
            odd1[a[i]] += 1
            odd2[b[i]] += 1
        else:
            eve1[a[i]] += 1
            eve2[b[i]] += 1

    if odd1 == odd2 and eve1 == eve2:
        print("YES")
    else:
        print("NO")