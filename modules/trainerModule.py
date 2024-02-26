import modules.menu as mn

def AddTrainer(rutas, salones, trainers:dict):

    mn.Clear()

    nombre = input('Ingrese el nombre:\n-> ')
    mn.Clear()
    print('\nIngrese el NOMBRE de la ruta en la que el trainer trabajara en la mañana:\n1. Java\n2. NodeJS\n3. NetCore\n')
    rutaMañana = input('\n-> ').lower()
    if rutaMañana in rutas:
        print('\nIngrese el NOMBRE del salon para la ruta en dicho horario:\n1. Apolo\n2. Artemis\n3. Sputnik\n')
        salonMañana = input('\n-> ').lower()
        if salonMañana in salones:
            print('\nIngrese el NOMBRE de la ruta en la que el trainer trabajara en la tarde:\n1. Java\n2. NodeJS\n3. NetCore\n')
            rutaTarde = input('\n-> ').lower()
            if rutaTarde in rutas:
                print('\nIngrese el NOMBRE del salon para la ruta en dicho horario:\n1. Apolo\n2. Artemis\n3. Sputnik\n')
                salonTarde = input('\n-> ').lower()
                if salonTarde in salones:
                    pass
                else:
                    print('El salon no se encuentra registrado.')
                    mn.Pause()
                    return
            else:
                print('La ruta no se encuentra registrada.')
                mn.Pause()
                return
        else:
            print('El salon no se encuentra registrado.')
            mn.Pause()
            return
    else:
        print('La ruta no se encuentra registrada.')
        mn.Pause()
        return


    trainer ={
        'nombre': nombre,
        'rutaMañana': rutaMañana,
        'salonMañana': salonMañana,
        'rutaTarde': rutaTarde,
        'salonTarde': salonTarde,
    }

    isTrue = True
    while isTrue:
        op = input('Desea ingresar otro trainer? Si (s) / No (Enter)\n-> ').lower()
        if op == 's':
            AddTrainer(rutas, salones, trainers)
        elif op == '':
            break

    mn.Clear()

    trainers.update({nombre:trainer})
    print(trainers)
    mn.Pause()