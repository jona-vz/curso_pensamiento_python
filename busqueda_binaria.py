#Aproximacion de una raiz cuadrada con diferencia de error epsilon aplicando una busqueda binaria para reducir el tiempo de ejecucion.

def raiz_cuadrada (objetivo, epsilon=0.001):
    '''
    Calcula una aproximacion de la raiz cuadrada del objetivo, con un error de epsilon

    param int objetivo  Cualquier numero entero que se quiera obtener su raiz caudrada
    param float epsilon Error minimo de aproximacion en la raiz. El valor por defecto es 0.01
    returns la raiz cuadrada de objetivo
    '''
    bajo = 0.0
    alto = max(1.0, objetivo)
    
    respuesta = (alto + bajo)/2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        #print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo =  respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo)/2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    return respuesta


if __name__=='__main__':
    objetivo = int (input ('Escoge un numero: '))
    respuesta = raiz_cuadrada(objetivo)


