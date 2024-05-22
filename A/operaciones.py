def suma(a,b):
    print(type(a))
    print(type(b))
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        print("a")
    #    print((type(a) == int or type(a) == float))
    #    print((type(b) == int or type(b) == float))
        return a+b
    else:
        print("b")
        print((type(a) == int or type(a) == float))
        print((type(b) == int or type(b) == float))
        print(TypeError)
        return TypeError

def resta(a,b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a-b
    else:
        return TypeError

def producto(a,b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a*b
    else:
        return TypeError

def division(a,b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        if b>0:
            return a+b
        else:
            return ZeroDivisionError
    else:
        return TypeError        
    
# try:
# # Intenta ejecutar este código
#     resultado = 10 / 0
# except ZeroDivisionError:
# # Si hay un error de división por cero, ejecuta esto
#     print("¡Oops! No se puede dividir por cero.")
# except Exception as e:
# # Puedes capturar cualquier otra excepción
#     print("Ocurrió un error:", e)
# else:
# # Este bloque se ejecuta si no hay excepciones
#     print("Todo salió bien.")
# finally:
# # Este bloque se ejecuta siempre, haya o no una excepción
#     print("Este es el bloque finally, se ejecuta siempre al final.")    