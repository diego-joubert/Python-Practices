import itertools
   import string

   def fuerza_bruta_password(password_real, longitud_maxima):
       caracteres = string.ascii_letters + string.digits + string.punctuation
       for longitud in range(1, longitud_maxima + 1):
           for intento in itertools.product(caracteres, repeat=longitud):
               intento = ''.join(intento)
               if intento == password_real:
                   return intento
       return None

   password_real = "abc123"
   longitud_maxima = 6
   print(f"Contraseña encontrada: {fuerza_bruta_password(password_real, longitud_maxima)}")