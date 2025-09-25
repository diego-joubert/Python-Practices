from math import pi
a = []
T = int(input())
i = 0;

while i<T:
    l = float(input())
    aq = l**2
    r = l/2
    ac = pi*(r**2)
    s = aq-ac
    a.append(s)
    i += 1
print("%.2f" %s)