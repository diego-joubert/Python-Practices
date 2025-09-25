def ecuacion(a, b, c):
    if a + b == c:
        return f"{a}+{b} = {c}"
    elif a - b == c:
        return f"{a}-{b} = {c}"
    elif a * b == c:
        return f"{a}*{b} = {c}"
    elif b != 0 and a / b == c:
        return f"{a}/{b} = {c}"
    if b+c == a:
        return f"{a}={b}+{c}"
    elif b-c == a:
        return f"{a}={b}-{c}"
    elif b*c == a:
        return f"{a}={b}*{c}"
    elif c != 0 and b/c == a:
        return f"{a}={b}/{c}"
    if c + a == b:
        return f"{b}={c}+{a}"
    elif c-a == b:
        return f"{b}={c}-{a}"
    elif c*a == b:
        return f"{b}={c}*{a}"
    elif a != 0 and c/a == b:
        return f"{b}={c}/{a}"

a, b, c = map(int, input().split())
resultado = ecuacion(a, b, c)
print(resultado)
        