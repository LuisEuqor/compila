# Definir el alfabeto
NUMEROS = set("0123456789")
LETRAS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
OPERADORES = set("+-*/")

# Definir los estados del AFD
estado_inicial = "inicial"
estado_numero = "número"
estado_palabra = "palabra"
estado_operador = "operador"
error = "error"
estado_final = {estado_numero, estado_palabra, estado_operador}

# Definir la función de transición
def transition(estado, simbolo):
    if estado == estado_inicial:
        if simbolo in NUMEROS:
            return estado_numero
        elif simbolo in LETRAS:
            return estado_palabra
        elif simbolo in OPERADORES:
            return estado_operador
        else:
            return error
    elif estado == estado_numero:
        if simbolo in NUMEROS:
            return estado_numero
        else:
            return estado_final.intersection({estado_numero}).pop()
    elif estado == estado_palabra:
        if simbolo in LETRAS or simbolo in NUMEROS:
            return estado_palabra
        else:
            return estado_final.intersection({estado_palabra}).pop()
    elif estado == estado_operador:
        return estado_final.intersection({estado_operador}).pop()
    else:
        return error

# Función principal del analizador léxico
def analizador(input_string):
    estado = estado_inicial
    lexema = ""
    token = ""
    for simbolo in input_string:
        nuevo_estado = transition(estado, simbolo)
        token += simbolo
        if nuevo_estado == error:
            return "Error: símbolo no válido"
        elif nuevo_estado in estado_final:
            return (nuevo_estado, lexema, token)

# Ejemplo de uso
entrada = "/"
resultado = analizador(entrada)
if resultado is not None:
    print("Token encontrado:", resultado)
else:
    print("Error léxico en la entrada") 