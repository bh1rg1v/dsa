# cook your dish here

for _ in range(int(input())):
    
    n = int(input())
    
    ans = n
    
    # if n % 3 == 2:
    #     ans = max(ans, n + 2)
    # if n % 3 == 1:
    #     ans = max(ans, n)
    # if n % 3 == 0:
    #     ans = max(ans, n + 1)
        
    if n == 1:
        print(1)
        continue
        
    if n % 2 == 0:
        ans = max(ans, n + n // 2 + 1)
    else:
        ans = max(ans, n + n // 2)
        
    print(ans)