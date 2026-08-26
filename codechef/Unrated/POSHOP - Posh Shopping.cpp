# cook your dish here

for t in range(int(input())):

    # n, k = map(int, input().split())
    n = int(input())
    
    a = list(map(int, input().split()))
    
    # a.sort()
    
    ans = max(a)
    
    val = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] <= a[j]:
                ans = max(ans, a[i] + a[j])
    
    print(ans)