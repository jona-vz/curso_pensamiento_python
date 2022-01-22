#Pruebas de caja de cristal
#Sabemos cual es el funcionamiento general de la funcion. Se prueban los distintos escenarios de respuesta individual. 

import unittest


def mayor_de_edad (edad):
    '''
    Devuelve True si la edad introducida es perteneciente a una persona mayor de edad

    param int edad cualquier edad positiva
    returns true si es mayor de 18 años. De lo contrario es false
    '''
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    #definimos los dos casos posibles, mayor y menor de edad    
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15
        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()