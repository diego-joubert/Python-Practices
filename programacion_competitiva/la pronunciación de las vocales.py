def sub_cadenas(cad):
    vocales = "aeiou"
    subcadenas = []
    
    for i in range(len(cad)):
        if cad[i] in vocales:
            j = 1
            while j < len(cad) and cad[j] in vocales:
                j += 1
            
            subcadenas.append(cad[i:j])
            i = j-1
    return subcadenas
    
cad = input()
substr = sub_cadenas(cad)
cad_orgullosa = [len(i) for i in substr]
print(max(cad_orgullosa))