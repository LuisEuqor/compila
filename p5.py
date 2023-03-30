class AFDNumero:
    def __init__(self):
        self.estado = 0
        
    def transicion(self, simbolo):
        if simbolo.isdigit():
            self.estado = 1
        elif simbolo == '.':
            self.estado = 2
        else:
            self.estado = -1
            
    def es_aceptado(self):
        return self.estado == 1 or self.estado == 2
class AFDPalabra:
    def __init__(self):
        self.estado = 0
        
    def transicion(self, simbolo):
        if simbolo.isalpha() or simbolo == '_':
            self.estado = 1
        elif simbolo.isdigit():
            self.estado = 2
        else:
            self.estado = -1
            
    def es_aceptado(self):
        return self.estado == 1 or self.estado == 2
class AFDOperador:
    def __init__(self):
        self.estado = 0
        
    def transicion(self, simbolo):
        if simbolo in ['+', '-', '*', '/', '%', '=', '<', '>']:
            self.estado = 1
        else:
            self.estado = -1
            
    def es_aceptado(self):
        return self.estado == 1
def analizador_lexico(cadena):
    simbolos = []
    lexema = ''
    tipo = ''
    
    for i in range(len(cadena)):
        afd_numero = AFDNumero()
        afd_palabra = AFDPalabra()
        afd_oper
