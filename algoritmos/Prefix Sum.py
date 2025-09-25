A = [1, 2, 3, 4, 5]
P = [0]* len(A)
P[0] = A[0]

for i in range(1, 5):
    P[i] = P[i-1] + A[i] #P = [0, 1, 3, 6, 10, 15]
    
#S(l, r) -> S(1, 3) = 9
for i in range(len(P)):
    print(f"Suma hasta el índice {i}: {P[i]} \n ")