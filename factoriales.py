#recursividad python

def factorial (n):
    """
    Calcula el factorial de n.

    param n int > 0
    returns n!
    """
    if n==1:
        return 1

    return n * factorial(n-1)

if __name__=='__main__':
    n = int(input ('Escribe un entero: '))
    print(factorial(n))