numero1, numero2 = map(float, input("Ingrese dos numeros: ").split())
operacion = input('Ingrese la operacion a realizar:')

if operacion == '+':
   print(numero1 + numero2)
elif operacion == '-':
    print(numero1 - numero2)
elif operacion == '*':
    print(numero1 * numero2) 
elif operacion == '/':
    print(numero1 / numero2)
else:
    print("Operacion invalida")