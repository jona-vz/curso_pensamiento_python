def nombre_completo (nombre, apellido, inverso=False):
    """
    Ordena el nombre completo, ya sea en orden (nombre - apellido) o invertido (apellido - nombre)

    param str nombre cualquier nombre
    param str apellido cualquier apellido
    returns la concatenacion del nombre y apellido en el orden requerido
    
    """
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'


res = nombre_completo ('Jona', 'Vasquez')
print (res)
res = nombre_completo ('Jona', 'Vasquez', inverso=True)
print (res)
res = nombre_completo (apellido='Vasquez', nombre='Jona')
print (res)