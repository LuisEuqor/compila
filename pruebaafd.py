# Definimos los Tokens
DIGITO = "[0-9]"
LETRA = "[a-zA-Z]"
SUMA = "["+"]"
RESTA = "[-]"
MULTIPLICACION = "[*]"
DIVISION = "[/]"
PARENTESIS_ABIERTO = "[(]"
PARENTESIS_CERRADO = "[)]"
ESPACIO_BLANCO = "[\s]"

# Creamos nuestro AFD para números enteros
AFD_NUM_ENTERO = {
    "q0": {DIGITO: "q1"},
    "q1": {DIGITO: "q1","default": "q2"},
    "q2": {}
}

# Creamos nuestro AFD para palabras
AFD_PALABRA = {
    "q0": {LETRA: "q1"},
    "q1": {LETRA: "q1",DIGITO: "q1","default": "q2"},
    "q2": {}
}

# Implementamos la función analizador_lexico
def analizador_lexico(cadena):
    estado_actual = "q0"
    token_actual = ""
    tokens = []

    for caracter in cadena:
        if caracter.isdigit():
            if estado_actual in AFD_NUM_ENTERO and DIGITO in AFD_NUM_ENTERO[estado_actual]:
                estado_actual = AFD_NUM_ENTERO[estado_actual][DIGITO]
                token_actual += caracter
            else:
                tokens.append(token_actual)
                token_actual = caracter
                estado_actual = "q1"
        elif caracter.isalpha():
            if estado_actual in AFD_PALABRA and LETRA in AFD_PALABRA[estado_actual]:
                estado_actual = AFD_PALABRA[estado_actual][LETRA]
                token_actual += caracter
            else:
                tokens.append(token_actual)
                token_actual = caracter
                estado_actual = "q1"
        else:
            if estado_actual in AFD_NUM_ENTERO:
                tokens.append(token_actual)
                token_actual = ""
                estado_actual = "q0"
            elif estado_actual in AFD_PALABRA:
                tokens.append(token_actual)
                token_actual = ""
                estado_actual = "q0"

    tokens.append(token_actual)

    return tokens

# Ejemplo de uso
cadena = "26 + 4 - 7 * (8 / 2) Hola mundo"
tokens = analizador_lexico(cadena)
print(tokens)
