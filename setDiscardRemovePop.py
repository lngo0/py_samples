n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    l1 = list(input().split())
    if l1[0] == "pop":
        s.pop()
    elif l1[0] == "remove":
        s.remove(int(l1[1]))
    elif l1[0] == "discard":
        s.discard(int(l1[1]))

sum1 = 0
for i in s:
    sum1 += i
print(sum1)
