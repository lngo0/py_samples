def is_strict_superset(a1, b1):
    return b.issubset(a1) and not (a1.issubset(b1))


a = set(int(i) for i in input().split(' '))
n = int(input())
res = True

for _ in range(n):
    b = set(int(j) for j in input().split(' '))
    res &= is_strict_superset(a, b)

print(res)
