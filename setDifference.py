n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))
s3 = s1.difference(s2)
count = 0
for i in s3:
    count += 1
print(count)
