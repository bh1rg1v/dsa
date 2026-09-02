# cook your dish here

from collections import Counter

for _ in range(int(input())):
    
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    ans = 1
    
    freq = Counter()
    
    for num in nums:
        msb = num.bit_length() - 1
        freq[msb] += 1
        
    for key, val in freq.items():
        ans = max(ans, val)
    
    print(ans)