# cook your dish here

from functools import lru_cache

rx, ry = 0, 0
p, q, r = 0, 0, 0

@lru_cache(maxsize=None)
def dfs(x, y):
    
    if x > rx or y > ry:
        return float("inf")
    
    if x == rx and y == ry:
        return 0
        
    a = dfs(x + 1, y) + p
    b = dfs(x + 2, y) + p
    
    c = dfs(x, y + 1) + q
    d = dfs(x, y + 2) + q
    
    e = dfs(x + 1, y + 1) + r
    
    return min([a, b, c, d, e])
        
    
for t in range(int(input())):

    a, b, p, q, r = map(int, input().split())
    
    rx, ry = a, b
    
    ans = dfs(0, 0)
    print(ans)
    
    dfs.cache_clear()