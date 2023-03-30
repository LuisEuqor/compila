alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0','1','3','4','5','6','7','8','+', '-', '*', '/']
#S estado inicial P estado para conocer palabras N estado para conocer numeros F estado final 
estados = {'S', 'P', 'N', 'F'}
def transicion(estado, simbolo):
    if estado == 'S':
        if simbolo.isalpha():
            return 'P'
        elif simbolo.isdigit():
            return 'N'
        elif simbolo in ['+', '-', '*', '/']:
            return 'F'
    elif estado == 'P':
        if simbolo.isalpha() or simbolo.isdigit():
            return 'P'
        else:
            return 'F'
    elif estado == 'N':
        if simbolo.isdigit():
            return 'N'
        elif simbolo == '.':
            return 'F'
        else:
            return 'F'
    elif estado == 'F':
        return 'F'
def analizador_lexico(cadena):
    estado_actual = 'S'
    buffer = ''
    tokens = []

    for simbolo in cadena:
        if simbolo in alfabeto:
            estado_siguiente = transicion(estado_actual, simbolo)
            if estado_siguiente == 'S':
                buffer = ''
            elif estado_siguiente == 'F':
                tokens.append((estado_actual, buffer))
                buffer = simbolo
            else:
                buffer += simbolo
            estado_actual = estado_siguiente
        else:
            raise ValueError(f"Símbolo no reconocido: {simbolo}")

    if buffer:
        tokens.append((estado_actual, buffer))

    return tokens
