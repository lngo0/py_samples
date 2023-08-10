n, m = map(int, input().split())

wc = 'WELCOME'
s1 = '.|.'
s2 = '-'
# upper part
for i in range(n//2):
    print((s1 * (i*2 + 1)).center(m, s2))
# middle part
print(wc.center(m, s2))
# lower part
for i in range(n//2 - 1, -1, -1):
    print((s1 * (i*2 + 1)).center(m, s2))
