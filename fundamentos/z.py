t = int(input())
r = []
for i in range(t):
    s = list(input())
    zs = s.count("z") + s.count("Z")
    if zs >= 3:
        r.append("Time to take a nap.")
    else:
        r.append("Perry saves the day!")
for i in range(len(r)):
    print(r[i])
    