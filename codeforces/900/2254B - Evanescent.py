
for t in range(int(input())):

    # n, m = map(int, input().split())
    n = int(input())
    
    # a = list(map(int, input().split()))

    s = input()

    ans = 0
    cnt = 0

    prev = "-"

    for ch in s:
        if prev != ch:
            cnt += 1
        else:
            pass
        prev = ch

    flag = False
    flag2 = False

    for i in range(n):

        if i == 0 or i == n - 1: continue

        if s[i] != s[i + 1] and s[i] != s[i - 1]:
            flag = True
            if s[i - 1] == s[i + 1]:
                flag2 = True

    # print(f"{t=}")
    # print(f"{flag=}")
    # print(f"{cnt=}")

    if flag:
        ans = cnt - 1
    else:
        ans = cnt

    if flag2:
        ans -= 1

    print(ans)

