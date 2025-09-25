cuenta = int(input("Por favor, ingrese la cuenta:"))

def calcular_propina(cuenta):
    propina = (cuenta * 15)/ 100
    print(f"La propina es de {propina} dolares")
    return propina

calcular_propina(cuenta)
    
    