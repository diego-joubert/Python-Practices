numero1 = float(input('Ingrese el primer numero:'))
numero2 = float(input('Ingrese el segundo numero:'))
if numero1 > numero2:
    print(f'{numero1} es mayor que {numero2}')
elif numero1 < numero2:
    print(f'{numero2} es mayor que {numero1}')
else:
    print(f'{numero1} y {numero2} son iguales.')