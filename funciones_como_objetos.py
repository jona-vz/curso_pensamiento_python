#Funciones como objetos
#En python las funciones son objetos, eso implica el paso por parametro

def multiplicar_por_dos (n):
    """
    Multiplica por dos a n

    n es un numero cualquiera
    returns n * 2 
    """
    return n*2

def sumar_dos (n):
    """
    Suma dos a n

    n es un numero cualquiera
    returns n + 2
    """
    return n+2

def aplicar_operacion (f, numeros):
    '''
    Recibe una operacion y la aplica a numeros.

    param f -- funcion para aplicar
    parm numeros -- lista de numeros cualquiera
    '''
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    
    return resultados

if __name__=='__main__':
    nums = [1, 2, 3]
    print(aplicar_operacion(multiplicar_por_dos, nums))

    print(aplicar_operacion(sumar_dos, nums))
