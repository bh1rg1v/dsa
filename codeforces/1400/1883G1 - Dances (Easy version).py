for _ in range(int(input())):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    a = [1] + a

    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 1 - 1

    idx = 0
    jdx = 0

    while idx < len(a) and jdx < len(b):

        if a[idx] < b[jdx]:
            idx += 1
            jdx += 1
        else:
            ans += 1
            a.pop()
            jdx += 1

    print(ans)