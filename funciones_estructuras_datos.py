#Tambien las funciones pueden se parte de una lista y ser listadas 'in'
def aplicar_operaciones (num):
    '''
    Aplica el 'abs' y el 'float' al numero recibido

    param int num cualquier numero
    returns una lista con las operaciones aplicadas
    '''
    operaciones = [abs, float]
    resultado = []

    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

if __name__=='__main__':
    print(aplicar_operaciones(-2))