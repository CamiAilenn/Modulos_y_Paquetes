def validar_rango(numero, desde, hasta)->float | int:
    '''Valida el numero en un rango, y lo pide indefinidamente hasta que este validado'''
    while numero<= desde or numero >= hasta:
        numero = int(input("Ingreso, no valido. Ingrese un numero: "))
    return numero

def validar_rango_una_vez(numero, desde, hasta)-> float | int | None:
    '''Valida un numero una unica vez, sino retorna None'''
    if numero<= desde or numero >= hasta:
        return None
    else:
        return numero