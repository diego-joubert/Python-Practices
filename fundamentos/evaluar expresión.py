expresion = list(input().split(";"))
x = 0

for i in range(len(expresion)):
    if expresion[i] == "X++" or expresion[i] == "++X":
        x += 1
    elif expresion[i] == "X--" or expresion[i] == "--X":
        x -= 1

print(x)