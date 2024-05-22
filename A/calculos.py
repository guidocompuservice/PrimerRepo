from operaciones import *
a, b, c, d = (10, 5, 0, "Hola")
try:
    print( "{} + {} = {}".format(a, b, suma(a, d) ) )
except Exception as e:    
#except TypeError as e:
    print("El tipo de dato ingresado no es válido \n###",e,"###")    
#print( "{} - {} = {}".format(b, d, resta(b, d) ) )
#print( "{} * {} = {}".format(b, b, producto(b, b) ) )
#print( "{} / {} = {}".format(a, c, division(a, c) ) )
else:
# # Este bloque se ejecuta si no hay excepciones
     print("Todo salió bien.")