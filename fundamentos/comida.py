comidas = {
   "Juan" : "tiburón en escabeche",
   "Pablo" : "paella don Beto", 
   "Alfredo" : "sesos de mono",
   "Fulano" : "cucarachas fritas",
   "Sonia" : "burros",
   "Lucas" : "hamburguesas Mr Paul",
   "Jose" : "ceviche",
   "Cesar" : "arroz con pollo"
}
afirmativas = set(['si','s','mucho','porfa'])
 
def saluda(nombre, comida):
    respuesta = input("Hola " + nombre + ", ¿te gusta " + comida + "? ")
    if respuesta not in afirmativas:
        pregunta(nombre)

def pregunta(nombre):
    respuesta = input("Hola " + nombre + ", ¿qué comida te gusta? ")
    comidas[nombre] = respuesta

for nombre in ["Juan", "Pablo", "Alfredo", "Fulano", "Sonia", "Lucas", "Mengano","Cesar"]:
    if nombre in comidas and comidas[nombre] is not None:
        saluda(nombre, comidas[nombre])
    else:
        pregunta(nombre)