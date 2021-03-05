
''' Instituto Tecnológico de Costa Rica
    Microprocesadores y Microcontroladores-Tarea 1

    Código que contiene los métodos check_char y caps_switch.
    codigo.py

    Castalia Leiva Cordero
    2018212665
'''


''' Función check_char() valida si su entrada es un solo carácter del alfabeto.
    Entrada: varible caracter que puede ser de cualquier tipo.
    Salidas: retorna cero si caracter es una letra del alfabeto, sino retorna
    un error único:
    113 si la entrada es más de un carácter, 3312 si el carácter no es una
    letra y 512 si la entrada no es un string.
'''


def check_char(caracter):

    if type(caracter) != str:  # compara si la variable es de tipo string
        return 512  # Error: el dato no es un string.
    else:
        if len(caracter) == 1:  # compara si el string tiene una longitud de 1
            if caracter.isalpha():  # compara si el string es alfabético
                return 0
            else:
                return 3312  # Error: el dato no es letra
        else:
            return 113  # más de un caracter


''' Función caps_switch(): convierte una letra mayúscula a minúscula y
    viceversa.
    Entrada: varible caracter que puede ser de cualquier tipo.
    Salidas: retorna la letra en mayúscula o minúscula o los errores únicos de
    la salida de la función check_char.
'''


def caps_switch(caracter):
    if check_char(caracter) == 0:  # ¿la variable en función check_char es 0?
        return caracter.swapcase()  # retorna mayúscula o minúscula
    else:
        return check_char(caracter)
