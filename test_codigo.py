
''' Instituto Tecnológico de Costa Rica
    Microprocesadores y Microcontroladores-Tarea 1

    Código que prueba las funciones de codigo.py por medio de pytest y asserts.
    test_codigo.py

    Castalia Leiva Cordero
    2018212665
'''


import codigo  # importación del arichivo codigo.py

# variable de tipo lista que contiene las letras del alfabeto en mayúsculas
listaMayus = ["A", "B", "C", "D", "E", "F", "G",  "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# variable de varios caracteres
palabra = "hola"

# variable string no alfabético
numero = "5"

# variable de tipo diferente a un string
no_string = 5

''' Función test_check_char(): valida valida si la función check_char() de
    codigo.py retorna 0 cuando esta tiene como entrada una letra. Funciona
    con un for que verifica las letras de la lista listaMayus y luego utiliza
    otro for pero cambiando cada letra de la lista por minúsculas. Luego se
    comprueba por medio de asserts.
    Entrada: no tiene entradas.
    Salidas: no tiene salidas.
'''


def test_check_char():
    for i in listaMayus:
        assert codigo.check_char(i) == 0  # verifica con mayusculas
    for i in listaMayus:
        assert codigo.check_char(i.lower()) == 0   # verifica con minúsculas


''' Función test_check_char_len(): valida valida si la función check_char()
    de codigo.py retorna 0 cuando esta tiene como entrada más de un carácter.
    Lo esperado es que sea un caso negativo.
    Entrada: no tiene entradas.
    Salidas: no tiene salidas.
'''


def test_check_char_len():
    assert codigo.check_char(palabra) == 0   # verifica varios caracteres.


''' Función test_check_char_letter(): valida valida si la función check_char()
    de codigo.py retorna 0 cuando esta tiene un carácter diferente a alguna
    letra. Lo esperado es que sea un caso negativo.
    Entrada: no tiene entradas.
    Salidas: no tiene salidas.
'''


def test_check_char_letter():
    assert codigo.check_char(numero) == 0   # verifica variable que no es letra


''' Función test_check_char_type(): valida valida si la función check_char()
    de codigo.py retorna 0 cuando esta tiene una entrada que no es un string.
    Lo esperado es que sea un caso negativo.
    Entrada: no tiene entradas.
    Salidas: no tiene salidas.
'''


def test_check_char_type():
    assert codigo.check_char(5) == 0   # verifica variable no string


''' Función test_caps_switch(): valida valida si la función caps_switch() de
    codigo.py retorna 0 cambia a minúscula si entrada es una mayúscula y
    viceversa. Verifica usando la variable listaMayus para que las invierta a
    minúscula y luego se trasnforma cada elemento de la lista para probar el
    caso contrario.
    Entradas: no tiene.
    Salidas: no tiene salidas.
'''


def test_caps_switch():
    for i in listaMayus:
        assert codigo.caps_switch(i) == i.lower()
    for i in listaMayus:
        assert codigo.caps_switch(i.lower()) == i
