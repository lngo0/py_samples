k, arr = int(input()), list(map(int, input().split()))

set1 = set(arr)

print(((sum(set1) * k) - (sum(arr))) // (k - 1))
