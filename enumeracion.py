#Enumeracion de resutados, probablemente la primera opcion en la busqueda de  resultados al tratarse de problemas sencillos

def raiz_cuadrada_entera (objetivo):
    '''
    Calcula una aproximacion de la raiz cuadrada ENTERA del objetivo

    param int objetivo  Cualquier numero entero que se quiera obtener su raiz caudrada
    returns la raiz cuadrada entera del objetivo, de no existir returns -1
    '''
    respuesta = 0
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        return -1
    else:
        print(f'{objetivo} no tiene una raiz cuadrada entera exacta')
        return respuesta


if __name__=='__main__':
    objetivo = int (input ('Escoge un entero: '))
    respuesta = raiz_cuadrada_entera(objetivo)

