def AddRuta(ejeTematico:dict):

    stack = input('Ingrese el Stack :')
    myStack ={
        'id' : str(len(ejeTematico)+1).zfill(2),
        'nombre' : stack
    }
    ejeTematico.update({myStack['id']:myStack})