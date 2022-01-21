# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    '''
    Devuelve un list con las primeras letras de cada palabra de la lista que se recibe. Por medio de asserts valída la el contenido del parametro.

    param   list lista_de_palabras Una lista de palabras donde todos los elementos sean de tipo str y no sean vacíos 
    '''
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacíos'

        primeras_letras.append(palabra[0])
    
    return primeras_letras


lista_palabras = ['People', 'likes', 'parties']
print(primera_letra(lista_palabras))