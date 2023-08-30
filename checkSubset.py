for _ in range(int(input())):
    t1, a, t2, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))