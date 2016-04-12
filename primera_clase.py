opc = 's'
while opc == 's':
    num1 = input('ingrese num1: ')
    num2 = input('ingrese num2: ')
    operacion = raw_input('1: suma, 2: resta ')
    if operacion == '1':
        print num1 + num2
    elif operacion == '2':
        print num1 - num2
    else:
        print "opcion invalida"

    opc = raw_input('volver a ejecutar?')
