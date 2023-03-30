alfabeto = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/="

transiciones = {
    0: {'DIGITO': 1, 'LETRA': 2, '+': 3, '-': 4, '*': 5, '/': 6, '=': 7},
    1: {'DIGITO': 1},
    2: {'DIGITO': 2, 'LETRA': 2},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {}
}
def analizador_lexico(entrada):
    estado_actual = 0
    token_actual = ""
    tokens = []

    for caracter in entrada:
        if caracter not in alfabeto:
            raise ValueError(f"Caracter no valido: {caracter}")
        if caracter.isdigit():
            simbolo = 'DIGITO'
        elif caracter.isalpha():
            simbolo = 'LETRA'
        else:
            simbolo = caracter

        if simbolo in transiciones[estado_actual]:
            estado_actual = transiciones[estado_actual][simbolo]
            token_actual += caracter
        else:
            if estado_actual in [1, 2]:
                tokens.append((token_actual, 'NUMERO' if estado_actual == 1 else 'PALABRA'))
            elif simbolo in ['+', '-', '*', '/', '=']:
                tokens.append((caracter, 'OPERADOR'))
            else:
                raise ValueError(f"Token no valido: {token_actual}")
           
