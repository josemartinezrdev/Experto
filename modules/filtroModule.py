import modules.menu as mn

def AddFiltro(matricula):
    mn.Clear()

    print(matricula)

    name = input('Ingrese el nombre del grupo al que le va a realizar el filtro\n-> ').upper()

    if name not in matricula:
        print('El grupo no se encuentra registrado')
        mn.Pause()
        return
    else:
        for i, items in enumerate(matricula[name]['campers']):
            print(f'{matricula[name]['campers'][i]['id']}: {matricula[name]['campers'][i]['nombre']}' )
        idSt = input('Ingrese la ID del estudiante al que le va a hacer el filtro\n-> ')

        noTeo = float(input('Ingrese nota Teórica para el camper\n-> '))
        if (noTeo > 0) and (noTeo <= 100):
            noPra = float(input('Ingrese nota Practica para el camper\n-> '))
            if (noPra > 0) and (noPra <= 100):
                noTrj = float(input('Ingrese nota de Trabajos para el camper\n-> '))
                if (noTrj > 0) and (noTrj <= 100):
                    promedio = (noTeo * 0.3) + (noPra * 0.6) + (noTrj * 0.1)
                    if promedio >= 60:
                        matricula[name]['campers'][i]['estado'] = 'Normal'
                    else:
                        matricula[name]['campers'][i]['estado'] = 'Bajo'
                else:
                    print('Nota no valida')
            else:
                print('Nota no valida')
        else:
            print('Nota no valida')
        
        print(matricula)
        mn.Pause()