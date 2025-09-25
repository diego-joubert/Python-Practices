def saludar(lang):
    def saludar_es():
        print("Hola")
    def saludar_en():
        print("Hi")
    def saludar_fr():
        print("Salut")
    
    lang_func = {"es": saludar_es,
                           "en": saludar_en,
                           "fr": saludar_fr}
    return lang_func[lang]
    
f = saludar(input("En que lenguaje quieres usar la funcion? (es, en, fr): "))
f()