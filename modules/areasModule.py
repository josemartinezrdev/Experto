import modules.menu as mn

def fillRoom(aula):
    for i, itm in aula.items():
        print('\nAula:\n')
        for j, value in itm.items():
            print(f'{j}: {value}')
        print('\n- - - - - - - - - - - -')
    mn.Pause()