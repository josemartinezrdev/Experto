"""
Estados: 
    Inscrito
    Admitido

    Bajo (< 60)
    Normal (>= 60)
"""

import modules.menu as mn

def AddCamper(campers:dict):
    id = input('Ingrese Id:\n-> ')
    mn.Clear()
    nombre = input('Ingrese el nombre:\n-> ')
    mn.Clear()
    apellido = input(f'Ingrese apellido de {nombre}\n-> ')
    mn.Clear()
    direccion = input(f'Ingrese la dirección de {nombre}:\n-> ')
    mn.Clear()
    estado = 'Inscrito'
    telefono = input(f'Ingrese el Teléfono:\n-> ')
    mn.Clear()

    camper ={
        'id': id,
        'nombre': nombre,
        'apellido': apellido, 
        'direccion': direccion,
        'estado': estado,
        'tel': telefono,
        'acudiente': {},
    }

    isTrue = True
    i = 0
    while isTrue:
        acudiente = input(f'Ingrese el acudiente:\n-> ')
        camper['acudiente'][i] = acudiente
        op = input('Desea ingresar otro acudiente? Si (s) / No (Enter)\n-> ')
        i += 1
        if i > 2:
            break
        if op.lower() == 's':
            continue
        elif op.lower() == '':
            break

    mn.Clear()

    campers.update({id:camper})

def DeleteCamperInicial(campers:dict, idxCamp):
    campers.pop(idxCamp)
    print(campers)

def AddEvaluation(campers:dict):
    isActive = True

    while isActive:

        idxCamp = input('Ingrese el ID del camper al que le vas a realizar la evaluación:\n-> ')
        mn.Clear()

        if idxCamp in campers:

            notaTeo = float(input('Ingrese nota teórica del camper: min: 0 / max: 100:\n-> '))
            mn.Clear()
            if (notaTeo < 0):
                print('La nota ingresada es menor a cero')
                AddEvaluation(campers)
            elif (notaTeo > 100):
                print('La nota ingresada es mayor a cien')
                AddEvaluation(campers)
            else:
                notaPra = float(input('Ingrese nota practica del camper: min: 0 / max: 100:\n-> '))
                mn.Clear()
                if (notaPra < 0):
                    print('La nota ingresada es menor a cero')
                    AddEvaluation(campers)
                elif (notaPra > 100):
                    print('La nota ingresada es mayor a cien')
                    AddEvaluation(campers)
                else:
                    promedio = (notaTeo + notaPra) / 2

                    if promedio >= 60:
                        campers[idxCamp]['estado'] = 'Admitido'

                        opt = input('Desea añadir la evaluación a otro camper? Si (s) / No (Enter)\n-> ')

                        if opt.lower() == 's':
                            continue
                        elif opt.lower() == '':
                            break

                    elif promedio < 60:
                        campers[idxCamp]['estado'] = 'Inscrito'
                        DeleteCamperInicial(campers, idxCamp)
                        mn.Pause()

                        opt = input('Desea añadir la evaluación a otro camper? Si (s) / No (Enter)\n-> ')

                        if opt.lower() == 's':
                            continue
                        elif opt.lower() == '':
                            break
