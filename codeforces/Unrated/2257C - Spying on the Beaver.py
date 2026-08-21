for _ in range(int(input())):
 
    n = int(input())
 
    parent = list(map(int, input().split()))
    parent = [-1] + parent
 
    m = int(input())
    dams = list(map(int, input().split()))
 
    dams.sort(reverse=False)
 
    print(m - 1, end=" ")
    print(*dams[1:])