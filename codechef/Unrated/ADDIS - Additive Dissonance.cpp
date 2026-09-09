# cook your dish here

from collections import Counter

for _ in range(int(input())):
    
    n = int(input())
    # n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    freq = Counter(nums)
    
    maxi = 0
    
    for k, v in freq.items():
        val = (v + 1) // 2
        maxi = max(maxi, val)
    
    print(maxi)