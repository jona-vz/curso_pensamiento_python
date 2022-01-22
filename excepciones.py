#Manejo de excepciones
#try - except

def divide_elementos_de_lista(lista, divisor):
    '''
    Divide por 'divisor' todos los elementos de una lista.

    param list lista de elementos que van a ser divididos
    param int, float divisor cualquier numero que dividirá la lista
    returns una lista con los elementos divididos por divisor. En caso de error returns la lista sin dividir
    '''
    #intenta realizar la division, pero si se encuentra con un error imprime el error y regresa la lista sin modificar.
    try:
        return [ i/divisor for i in lista]
    except ZeroDivisionError as e:
        print (e)
        return lista


if __name__=='__main__':
    lista = list(range(10))
    divisor = 0
    print(divide_elementos_de_lista(lista, divisor))
