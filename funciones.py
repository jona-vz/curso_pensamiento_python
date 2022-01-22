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

if __name__=='__main__':
    print('Con parametros normales sin invertir')
    res = nombre_completo ('Jona', 'Vasquez')
    print (res)
    
    print('Con parametros normales invetido')
    res = nombre_completo ('Jona', 'Vasquez', inverso=True)
    print (res)

    print('Con parametros invertidos pero el nomrbre sin invertir')
    res = nombre_completo (apellido='Vasquez', nombre='Jona')
    print (res)