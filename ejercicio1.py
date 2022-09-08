# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente 
# y separados por comas.


def main():
    paises = input('Introduzca una serie de paises separados por coma')
    listaPaises = paises.split(',') #Convertimos el string en una lista
    setPaises = set(listaPaises)    #pasamos la lista a set para eliminar duplicados
    #print(setPaises)
    listaPaises = list(setPaises)   #Volvemos a convertir el set en lista para aplicar sorted()
    print(sorted(listaPaises))      #Ordenamos y mostramos el resultado por pantalla


if __name__ == "__main__":
    main()           
