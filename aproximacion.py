#Aproximacion de una raiz cuadrada con diferencia de error epsilon

def raiz_cuadrada (objetivo, epsilon=0.01):
    '''
    Calcula una aproximacion de la raiz cuadrada del objetivo, con un error de epsilon

    param int objetivo  Cualquier numero entero que se quiera obtener su raiz caudrada
    param float epsilon Error minimo de aproximacion en la raiz. El valor por defecto es 0.01
    returns la raiz cuadrada de objetivo
    '''
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #print(abs(respuesta**2 - objetivo), respuesta)

        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

    return respuesta
    


if __name__=='__main__':
    objetivo = int (input ('Escoge un entero: '))
    resultado = raiz_cuadrada(objetivo)