import modules.menu as mn

def AddGroup(campers, areas, trainers, matricula):

    lstCampers = []

    nombre = input('Ingrese el nombre del grupo que va a matricular:\n-> ').upper()
    nombreTrainer = input(f'Ingrese el nombre del trainer para el grupo {nombre}:\n-> ')

    if nombreTrainer not in trainers:
        return
    else:
        horario = input(f'Ingrese el índice del horario en el que trabaja el trainer:\n1. J. Mañana ({trainers[nombreTrainer]['rutaMañana']} - {trainers[nombreTrainer]['salonMañana']})\n2. J. Tarde ({trainers[nombreTrainer]['rutaTarde']} - {trainers[nombreTrainer]['salonTarde']})\n-> ')
        i = horario
        if horario == '1':
            horario = f'J. Mañana ({trainers[nombreTrainer]['rutaMañana']} - {trainers[nombreTrainer]['salonMañana']})'
        elif horario == '2':
            horario = f'J. Tarde ({trainers[nombreTrainer]['rutaTarde']} - {trainers[nombreTrainer]['salonTarde']})'
        else: 
            print('El horario no es valido, los trainers deben descansar. 💤')
            mn.Pause()
            return
        
        fechaInit = input('Ingrese la fecha de inicio en el siguiente formato: día/mes/año\n-> ')
        fechaEnd = input('Ingrese la fecha de finalización en el siguiente formato: día/mes/año\n-> ')

        def Add(lstCampers, campers):
            camper = input('Ingrese el ID del camper para añadir a este grupo: (El camper debe estar "Admitido")\n-> ')
            if camper not in campers:
                return
            else:
                if (campers[camper]['estado']).lower() == 'admitido':
                    lstCampers.append(campers[camper])
        
        Add(lstCampers, campers)


        grupo = {
            'nombre': nombre,
            'nombreTrainer': nombreTrainer,
            'horario': horario,
            'fechaInit': fechaInit,
            'fechaEnd': fechaEnd,
            'campers': lstCampers
        }

        if i == '1':
            h = trainers[nombreTrainer]['salonMañana']
        elif i == '2':
            h = trainers[nombreTrainer]['salonTarde']

        if len(lstCampers)-1 < areas[h]['capacidad']:
            isTrue = True
        else:
            isTrue = False
        while isTrue:
            op = input('Desea ingresar otro camper? Si (s) / No (Enter)\n-> ').lower()
            if op == 's':
                Add(lstCampers, campers)
            elif op == '':
                break

        mn.Clear()

        matricula.update({nombre:grupo})
        mn.Pause()
