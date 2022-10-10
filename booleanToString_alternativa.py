'''
La funcion recibe un valor booleano 0 o 1
y de vuelve un string True o False segun sea el caso

Python reconoce como true cualquier valor excepto el cero y false. 
'''
def boolean_to_string(b):
    if b:
        return('True')
    else:
        return('False')