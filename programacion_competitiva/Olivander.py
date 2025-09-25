def entran_en_la_caja(varitas, cajas):
    varitas.sort()
    cajas.sort()
    
    for varitas, cajas in zip(varitas, cajas):
        if varitas > cajas:
            return "NE"
    return "DA"

N = int(input())
varitas = list(map(int, input().split()))
cajas = list(map(int, input().split()))

resultado = entran_en_la_caja(varitas, cajas)
print(resultado)