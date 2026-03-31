""" Ejercicio 1 de la serie de Hash Table: Contador de palabras mejorado """

def contar_palabras(texto):
    """ 
    Cuenta palabras, pero:
    
    1. Ignora mayúsculas/minúsculas 
    2. Ignora puntuación 
    3. Devuelve las 10 palabras más comunes """

    from collections import Counter
    import re

    palabras = re.sub(r'[^\w\s]', ' ', texto.lower()).split()
    contador = Counter(palabras)
    palabras_mas_comunes = contador.most_common(10)

    return palabras_mas_comunes

texto_prueba = """ 
        Python es un lenguaje de programación. 
        Python es interpretado, python es multiparadigma. 
        ¡Python es genial! Python, python, PYTHON. 
        """

resultado = dict(contar_palabras(texto_prueba))
print(resultado)