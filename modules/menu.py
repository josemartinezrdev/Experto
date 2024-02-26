import os


def Clear():
    osy = os.name

    if osy == 'nt':
        os.system('cls')
    elif osy == 'posix':
        os.system('clear')


def Pause():
    osy = os.name

    if osy == 'nt':
        os.system('pause')
    elif osy == 'posix':
        os.system('pause')


def CreateMenu():

    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    msg = """
    
        Ingrese una opción:

        1. Registrar camper #¿ Listo
        2. Registrar Prueba Ingreso #¿ Listo
        3. Registrar ruta #¿ Listo
        4. Registrar Trainer #¿ Listo
        5. Listar aulas #¿ Listo
        6. Matricula #¡ Progreso
        7. Registrar filtro #! NADA
        8. Reportes #! NADA
        9. Salir #¿ Listo
    
    """

    print(msg)
    opt = input('\n-> ')
    Clear()

    while opt not in options:
        Clear()
        print('La opción no es válida')
        print(msg)
        opt = input('Ingresa la opción nuevamente\n-> ')
        Clear()
    return opt
