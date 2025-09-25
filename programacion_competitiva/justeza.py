A, B, C, k = map(int, input().split())
for i in range(k):
    a, b, c = A, B, C
    A = b+c
    B = c+a
    C = a+b
if abs(A-B) > 10**18:
    print("Unfair")
else:
    print(A-B)