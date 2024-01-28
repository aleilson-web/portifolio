# Design grafico

import math
from turtle import*


def coracaoA(k):
    return 12*math.sin(k)**3
def coracaoB(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
                math.cos(3*k)-\
                math.cos(4*k)

speed(60)


# Cor de fundo
bgcolor("Black")

# Número de voltas do cursor
for i in range(100000):

    # Definindo tamanho
    goto(coracaoA(i)*10, coracaoB(i)*10)

    # Alterando velocidade das linhas 
    for j in range(5):
        color("#f73487")
        goto(0,0)
done()
