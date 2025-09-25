c1, c2, c3 = map(int, input().split())
if c1 != c2 and c2 != c3 and c1 != c3:
    print(1)
elif c1 == c2 and c2 == c3 and c1 == c3:
    print(3)

elif c1== c2 and c2 != c3 and c1 != c3 or c2 == c3 and c1 != c2 and c1 != c3 or c1 == c3 and c3 != c2 and c2 != c1:
    print(2)