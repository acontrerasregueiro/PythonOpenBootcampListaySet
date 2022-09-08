#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares 
# de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce  #Necesario para el modulo reduce


def obtenerImpares(a):
    if (a % 2) == 0:
        return False
    return True
    

def hacerSumatorio(a,b):
    return a + b

def main():

    #Metodo largo, pasando funcion
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    impares = filter(obtenerImpares,lista)
    print('Listado de numeros impares ',list(impares))
    #Metodo corto, con lambda
    impares = filter(lambda x:x % 2 != 0,lista)
    print('Listado de numeros impares ',list(impares))
    ############################################################
    
    #Calcular sumatorio con reduce y lambda
    sumatorio = reduce(lambda a,b: a + b,lista)
    print('El sumatorio de todos los numeros de la lista es : ',sumatorio)
    #Calcular sumatorio con reduce y una funcion
    sumatorio = reduce(hacerSumatorio,lista)
    print('El sumatorio de todos los numeros de la lista es : ',sumatorio)
    
    


if __name__ == "__main__":
    main()           
