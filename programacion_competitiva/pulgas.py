s = input()
pm, pb = 0, 0
v = ["A", "E", "I", "O", "U"]
for i in range(len(s)):
    if s[i] in v:
        pm += 1
    else:
        continue
for i in range(len(s)):
    if not s[i] in v:
        pb += 1
    else:
        continue
print(f"{pm} {pb}")