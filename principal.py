
import modules.camperModule as camp     #- 1
import modules.rutasModule as rut       #- 2
import modules.menu as mn               #- 3
import modules.areasModule as am        #- 4
import modules.trainerModule as tr      #- 5
import modules.matriculaModule as mt    #- 6
import modules.filtroModule as ft       #- 7

if __name__ == '__main__':

    campus = {
        'campers':{},
        'rutas':{
            'java':{
                'fundamentos':{},
                'web':{},
                'lenFormal':{},
                'dataBases':{},
                'backend':{}
            },
            'nodejs':{
                'fundamentos':{},
                'web':{},
                'lenFormal':{},
                'dataBases':{},
                'backend':{}
            },
            'netcore':{
                'fundamentos':{},
                'web':{},
                'lenFormal':{},
                'dataBases':{},
                'backend':{}
            }
        },
        'areas':{
            'apolo':{
                'nombre':'Apolo',
                'capacidad':33
            },
            'artemis':{
                'nombre':'Artemis',
                'capacidad':35
            },
            'sputnik':{
                'nombre':'Sputnik',
                'capacidad':36
            }
        },
        'trainers':{},
        'matricula':{}
    }

    # print(json.dumps(campus, indent=4))
    # lstRutas = list(campus['rutas'].keys())
    # print(lstRutas)
    # print(json.dumps(campus, indent=4))

    isRunning = True

    while isRunning:

        mn.Clear()
        opt = mn.CreateMenu()

        if opt == '1': #* Registrar camper
            camp.AddCamper(campus.get('campers'))
        elif opt == '2': #* Registrar nota inicial
            camp.AddEvaluation(campus.get('campers'))
        elif opt == '3': #* Registrar ruta
            rutaD = input('Ingrese la Ruta:\n-> ').lower()
            eje = input('Ingrese el eje tematico\n-> ').lower()
            rut.AddRuta(campus.get('rutas').get(rutaD).get(eje))
        elif opt == '4': #* Registrar Trainer
            tr.AddTrainer(campus.get('rutas'), campus.get('areas'), campus.get('trainers'))
        elif opt == '5': #* Ver aulas
            am.fillRoom(campus.get('areas'))
        elif opt == '6': #* Matricula
            mt.AddGroup(campus.get('campers'), campus.get('areas'), campus.get('trainers'), campus.get('matricula'))
        elif opt == '7': #¡ Filtro
            ft.AddFiltro(campus.get('matricula'))
        elif opt == '8': #! Reportes
            pass 
        elif opt == '9': #* Salir
            isRunning = False