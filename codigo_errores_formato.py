
''' Instituto Tecnológico de Costa Rica
    Microprocesadores y Microcontroladores-Tarea 1

    Código reescribe arreglando los erroes de codigo_errores_formato.py
    codigo_errores_corregido.py

    Castalia Leiva Cordero
    2018212665
'''


''' Función operaciones: suma o resta dos enteros
    Entradas: operación, entero que será 1 para efectuar una suma o 2 para
    restar,y ent1 y ent2 que son dos números para aplicar la operación.
    Salidas: retorna el cálculo respectivo, retornará un string si las entradas
    no coinciden con los datos deseados.
'''


def operaciones(operacion, ent1, ent2):
    if type(operacion) != int or type(ent1) != int or type(ent2) != int:
        # revisa si son enteros
        return "error"
    else:
        if operacion == 1:
            return ent1 + ent2
        elif operacion == 2:
            return ent1 - ent2
        else:
            return "error"
