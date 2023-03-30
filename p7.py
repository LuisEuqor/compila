# Definir el alfabeto
ALFABETO = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/")

# Definir los estados
ESTADO_INICIAL = "inicial"
ESTADO_NUMERO = "numero"
ESTADO_PALABRA = "palabra"
ESTADO_OPERADOR = "operador"
ESTADOS_ACEPTACION = {ESTADO_NUMERO, ESTADO_PALABRA, ESTADO_OPERADOR}

# Definir la función de transición
def transicion(estado, caracter):
    if caracter.isdigit():
        return ESTADO_NUMERO
    elif caracter.isalpha():
        return ESTADO_PALABRA
    elif caracter in {"+", "-", "*", "/"}:
        return ESTADO_OPERADOR
    else:
        return None

# Implementar el AFD
def analizador_lexico(cadena):
    estado_actual = ESTADO_INICIAL
    token = ""
    for caracter in cadena:
        if caracter not in ALFABETO:
            break
        estado_actual = transicion(estado_actual, caracter)
        token += caracter
        if estado_actual is None:
            break
    if estado_actual in ESTADOS_ACEPTACION:
        return (estado_actual, token)
    else:
        return None

# Ejemplo de uso
entrada = "*"
resultado = analizador_lexico(entrada)
if resultado is not None:
    print("Token encontrado:", resultado)
else:
    print("Error léxico en la entrada")
