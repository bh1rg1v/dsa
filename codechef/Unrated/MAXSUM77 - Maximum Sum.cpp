# cook your dish here

for _ in range(int(input())):
    
    n, k = map(int, input().split())
    
    nums = list(map(int, input().split()))
    
    ans = 0
    total = sum(nums)
    
    for i in range(k + 1):
        
        x = i
        y = k - x
        
        new = nums[:x]
        if y:
            new += nums[-y:]
            
        # print(x, y, new)
        
        rem = sum(new)
        val = total - rem
        
        ans = max(ans, val)
    
    print(ans)