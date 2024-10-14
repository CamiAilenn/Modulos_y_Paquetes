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
    
def mostrar_lista(lista:list):
    "Muestra una lista con un for"
    for i in range (len(lista)):
        print(lista[i])

def swapear_lista(lista:list, posicion_primera:int, posicion_segunda:int)->list:
    """ingresa una lista y dos posiciones por parametro, e intercambia las posiciones
    retorna la nueva lista con las posiciones intercambiadas"""
    aux = lista[posicion_primera]
    lista[posicion_primera] = lista[posicion_segunda]
    lista[posicion_segunda] = aux

def agregar_datos_a_lista(lista:list, cantidad:int):
    """Agrega datos a una lista,
    la cantidad de datos es indicada por el usuario"""
    lista = []
    for i in range(cantidad):
        dato = input("Ingrese el dato a agregar a la lista ")
        lista.append(dato)
    return lista

def posicion_menor_numero(lista:list)->int:
    """Busca al mayoor numero de una lista
    retorna la posicion que ocupa"""
    menor = lista[0]
    posicion_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicion_menor = i
    return posicion_menor

def posicion_mayor_numero(lista:list)->int:
    """Busca el mayor numero de una lista
    retorna la posicion que ocupa"""
    mayor = lista[0]
    posicion_mayor = 0
    for i in range(len(lista)):
        if lista[i] < mayor:
            mayor = lista[i]
            posicion_mayor = i
    return posicion_mayor

def promedio(lista:list):
    "Ingresa una lista por parametro y calcula el promedio"
    acumulador = 0
    promedio = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    promedio = acumulador / len(lista)
    return promedio
#PARA TABULARRRRR
"""def mostrar_uno(productos:list, pos:int):
    'Muestra un solo producto con su nombre, cantidad y ubicacion.'
    print(f'{productos[pos][0]:<12}  {productos[pos][1]:<10}    {productos[pos][2]}')"""