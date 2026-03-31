"""

Implementaciones para la estructura de datos Hash Table, contiene:
    - Implementacion basica con funcionamiento minimo 
    - Implementacion con manejo de colisiones usando encadenamiento (Chaining)
    - Implementacion con manejo de colisiones usando direccionamiento abierto (Open Addressing)

"""

# 1. Hash Table basica sin manejo de colisiones

class HashTable:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]
        self.tamano = 0

    def _hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        indice = self._hash(clave)

        for i, (k, v) in enumerate(self.tabla[indice]):
            if k==clave:
                self.tabla[indice][i] = (clave, valor)
                return

        self.tabla[indice].append((clave, valor))
        self.tamano += 1

        if self.tamano / self.capacidad > 0.7:
            self._redimensionar()
    
    def obtener(self, clave):
        indice = self._hash(clave)

        for k, v in self.tabla[indice]:
            if k==clave:
                return v

        raise KeyError(f"Clave {clave} no encontrada.")

    def eliminar(self, clave):
        indice = self._hash(clave)

        for i, (k, v) in enumerate(self.tabla[indice]):
            if k==clave:
                del self.tabla[indice][i]
                self.tamano -= 1
                return

        raise KeyError(f"Clave {clave} no encontrada. ")

    def _redimensionar(self):
        vieja_tabla = self.tabla
        self.capacidad *= 2
        self.tabla = [[] for _ in range(self.capacidad)]
        self.tamano = 0

        for bucket in vieja_tabla:
            for clave, valor in bucket:
                self.insertar(clave, valor)

    
    def __str__(self):
        resultado = []

        for i, bucket in enumerate(self.tabla):
            if bucket:
                resultado.append(f"Bucket {i}:{bucket}")

        return "\n".join(resultado)


# 2. Hash Table con manejo de colisiones usando chaining

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        sel.siguiente = None

class HashTableEncadenada:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.tamano = 0

    def _hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        indice = self._hash(clave)

        if self.tabla[indice] is None:
            self.tabla[indice] = Nodo(clave, valor)

        else:
            actual = self.tabla[indice]

            while actual:
                if actual.clave == clave:
                    actual.valor = valor
                    return

                if actual.siguiente is None:
                    break
                actual = actual.siguiente

            actual.siguiente = Nodo(clave, valor)
            self.tamano += 1

    def buscar(self, clave):
        indice = self._hash(clave)
        actual = self.tabla[indice]

        while actual:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente

        return None

    def mostrar(self):
        for i in range(self.capacidad):
            print(f"Bucket {i}: ", end=" ")
            actual = self.tabla[i]
            while actual:
                print(f"[{actual.clave}:{actual.valor}] -> ", end=" ")
                actual = actual.siguiente


# 3. HashTable con manejo de colisiones usando open addressing

class HashTableOpenAddressing:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.tamano = 0

    def _siguiente_indice(self, indice, intento):
        return (indice + intento) % self.capacidad

    def insertar(self, clave, valor):
        if self.tamano >= self.capacidad:
            self._redimensionar()

        intento = 0
        indice = hash(clave) % self.capacidad

        while self.tabla[indice] is not None:
            if self.tabla[indice][0] == clave:
                self.tabla[indice] = (clave, valor)
                return

            intento += 1
            indice = self._siguiente_indice(indice, intento)

        self.tabla[indice] = (clave, valor)
        self.tamano += 1

ht = HashTable()
ht.insertar("Diego", 15)
ht.insertar("Juan", 17)
ht.insertar("Samanta", 13)
ht.insertar("nauJ", 14)
print(ht)
ht.insertar("Diego", 16)
print(ht)
print(ht.obtener("Diego"))
ht.eliminar("nauJ")
print("\n", ht)
