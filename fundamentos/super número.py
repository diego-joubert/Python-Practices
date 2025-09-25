MOD = 34047161064
v, k, n = map(int, input().split())

l, d = len(str(n)), len(str(n))
s = sum(map(int, str(n)))

for i in range(k):
    d = d + (d-1) * l
    s = s + (d-1) * s

print(s)
if v == 1:
    print(d%MOD)
else:
    print(d%MOD)
    if s%3 == 0:
        print("SI")
    else:
        print("NO")