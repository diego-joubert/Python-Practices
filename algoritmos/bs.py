def busqueda_binaria(arr, objetivo):
    inf = 0
    sup = len(arr) - 1
    
    while inf <= sup:
        mitad = inf + (sup - inf) // 2
        
        if arr[mitad] == objetivo:
            return mitad
        elif arr[mitad] < objetivo:
            inf = mitad + 1
        else:
            sup = mitad - 1
    return -1