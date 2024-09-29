from Validate import *

def get_int(bienvenida:str, mensaje_error:str, minimo:int, maximo:int, intentos:int)->int | None:
    '''Da la bienvenida, pide un numero entero,
    usa la funcion de validacion de Validate para validarlo en un rango 
    lo hace la cantidad de intentos que indica el usuario, si no lo valida, 
    printea el mensaje de error'''
    print(bienvenida)
    for i in range(intentos):
        numero = int(input("Ingrese un numero entero: "))
        validacion = validar_rango_una_vez(numero, minimo, maximo)
        if validacion == None:
            print(mensaje_error)
        else:
            return  numero
        
def get_float(bienvenida:str, mensaje_error:str, minimo:float, maximo:float, intentos:int)->float | None:
    '''Da la bienvenida, pide un numero flotante,
    usa la funcion de validacion de Validate para validarlo en un rango 
    lo hace la cantidad de intentos que indica el usuario, si no lo valida, 
    printea el mensaje de error'''
    print(bienvenida)
    for i in range(intentos):
        numero = int(input("Ingrese un numero flotante: "))
        validacion = validar_rango_una_vez(numero, minimo, maximo)
        if validacion == None:
            print(mensaje_error)
        else:
            return  numero


def get_string(cadena:str, mensaje_error:str, minimo:float, maximo:float, intentos:int)->str | None:
    '''Ingresa la cadena str por parametro, cuenta los caracteres con la funcion len
    usa la funcion de validacion de Validate para validar que la cantidad de caracteres
    este en el rango establecido
    lo hace la cantidad de intentos que indica el usuario, si no lo valida, 
    printea el mensaje de error'''
    for i in range(intentos - 1):   # menos 1 porque ya entra la primera vez por parametro
        cantidad_caracteres = len(cadena)
        validacion = validar_rango_una_vez(cantidad_caracteres, minimo, maximo)
        if validacion == None:
            print(mensaje_error)
            cadena = str(input("Reingrese la cadena a validar: "))
        else:
            return cadena
    
