def max_valor(n):
    digits = str(n)
    d1 = int(digits[0])
    d2 = int(digits[1])
    d3 = int(digits[2])
    
    results = []
    
    results.append((d1+d2)+(d2*d3))
    results.append((d1*d2)+(d2+d3))
    
    return max(results)

num = int(input())
print(max_valor(num))