'''
Potenciação

Divisão

Multiplicação

Soma

Subtração
'''


def calcular_media(numeros):

    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def e_par(numero):
    return numero % 2 == 0


def soma(a, b):

    return a + b

def subtrair(a, b):

    return a - b

def multiplicar(a, b):

    return a * b


def potencia(a, expoente):
    """Eleva a base exponte."""

    return a ** expoente


def resto_divisao(a, b):
    """Calcula o resto da divisão (módulo)."""
    
    return a % b


