#Pruebas de caja negra
#No sabemos cual es el funcionamiento general de la funcion. Pero si sabemos cuales son los resultados. Se prueban los distintos escenarios de respuesta individual. 

import unittest
from unittest import result

def suma(num_1, num_2):
    '''
    Realiza la suma de dos numeros enteros

    param int num_1 cualquier numero entero
    param int num_2 cualquier numero entero
    returns el resultado de la suma entre num_1 y num_2
    
    '''
    return num_1 + num_2

class CajaNegraTest (unittest.TestCase):
    #checar el procedimiento de sumar dos positivos
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma (num_1, num_2)

        self.assertEqual(resultado, 15)

    #checar el procedimiento de sumar dos negativos
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma (num_1, num_2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()

