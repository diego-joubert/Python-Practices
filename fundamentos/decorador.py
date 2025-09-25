def mi_decorador(funcion):
    def nueva(*args):
        print("Llamada a la funcion", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nueva
    
@mi_decorador
def imp(x):
    print(x)
    
imp(input("Ingrese un texto: "))