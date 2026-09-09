# cook your dish here

for _ in range(int(input())):
    
    n = int(input())
    # n, k = map(int, input().split())
    # nums = list(map(int, input().split()))
    
    a = input()
    b = input()
    
    ca = a.count("a") + b.count("a")
    cb = a.count("b") + b.count("b")
    
    if ca == cb:
        print("Yes")
    else:
        print("No")