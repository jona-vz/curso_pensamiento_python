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
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    
    return resultados

nums = [1, 2, 3]
print(aplicar_operacion(multiplicar_por_dos, nums))

print(aplicar_operacion(sumar_dos, nums))
