def generar_primos():
    """ Generador que produce numeros primos infinitamente """

    primos = []
    candidato = 2 # Primer numero primo

    while True:
        es_primo = True

        for primo in primos:
            if primo*primo > candidato:
                break
            if candidato%primo == 0:
                es_primo = False
                break
        
        if es_primo:
            primos.append(candidato)
            yield candidato
        candidato += 1

# Prueba: Vamos a mostrar solo los primos menores que 100
for primo in generar_primos():
    if primo > 100:
        break
    print(primo)