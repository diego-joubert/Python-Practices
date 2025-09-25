a = input()
b = input()
c = 0

for i in a:
    c1 = 0
    c1 += min(a.count(i), b.count(i))
for i in b:
    c2 = 0
    c2 += min(a.count(i), b.count(i))
c = max(c1, c2)
print(c)