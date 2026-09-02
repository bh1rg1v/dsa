# cook your dish here

for _ in range(int(input())):
    
    n = int(input())
    
    val = n % 2
    ans = (n // 2) * 30
    
    if val:
        ans += 20
        
    print(ans)