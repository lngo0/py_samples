from collections import Counter

X = int(input())
shoe_list = list(map(int, input().split()))
shoe_size = Counter(shoe_list)
N = int(input())
total = 0

for _ in range(N):
    x, m = map(int, input().split())
    if x in shoe_size:
        if shoe_size[x] > 0:
            total += m
            shoe_size[x] = shoe_size[x] - 1

print(total)
