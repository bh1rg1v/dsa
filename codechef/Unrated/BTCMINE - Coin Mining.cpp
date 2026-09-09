# cook your dish here

from functools import lru_cache

for t in range(int(input())):
    
    # n = int(input())
    x, y = map(int, input().split())
    # nums = list(map(int, input().split()))
    
    # print(f"Testcase: {t=}")
    
    day = 0
    
    cost = 0
    earned = 0
    
    maxi = 0
    
    while True:
        
        day += 1
        
        cost += x
        earned += y * (day * day)
        
        # print(cost, earned)
        
        if earned > cost:
            # print(day)
            maxi = day
            break
        
    ans = float("inf")
        
    @lru_cache(maxsize=None)
    def dp(day, cost, earned, gpuCnt):
        
        # print(day, cost, earned, gpuCnt)
        
        # print(f"{earned=} {cost=}")
        
        global ans
        
        if day >= maxi + 2: return False
        
        if earned > cost:
            ans = min(ans, day)
            # print("Here")
            return True
        
        nearned = earned + y * ((gpuCnt + 1) * (gpuCnt + 1))
        
        pick = dp(day + 1, cost + x, nearned, gpuCnt + 1)
        
        nearned = earned + y * (gpuCnt * gpuCnt)
        notPick = dp(day + 1, cost, nearned, gpuCnt)
        
        return (pick or notPick)
        
    dp(0, 0, 0, 0)
    dp.cache_clear()
    
    print(ans)