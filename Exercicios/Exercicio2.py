import random

# Definindo o baralho completo
naipes = ["Espadas", "Copas", "Ouros", "Paus"]
valores = list(range(1, 14))  # Cartas de 1 (ás) a 13 (rei)
baralho = [(valor, naipe) for naipe in naipes for valor in valores]

# Separando e embaralhando apenas as cartas de Espadas
cartas_espadas = [(valor, "Espadas") for valor in valores]
random.shuffle(cartas_espadas)

def ordenar_cartas(cartas):
    # "Primeira mão" que mantém as cartas ordenadas
    mao = []

    for carta in cartas:
        # Condição (b) e (c): Somente uma carta é visível por vez e ela é "retirada" da pilha para ser colocada na posição correta na "mão"

        # Encontrar a posição correta para a carta na "mão" (mantendo a ordem crescente)
        posicao_inserir = 0
        while posicao_inserir < len(mao) and mao[posicao_inserir][0] < carta[0]:
            posicao_inserir += 1

        # Condição (d) e (e): Inserir a carta na frente ou atrás da pilha na posição correta para manter a ordem, simulando os dedos segurando a carta
        # A outra mão só segura uma carta por vez (feito implicitamente ao inserir)
        mao.insert(posicao_inserir, carta)


    # Condição (a): Todas as cartas estão em uma única "mão".
    return mao

# Condição (f): Todas as cartas estão ordenadas em uma única "mão" ao final
mao_ordenada = ordenar_cartas(cartas_espadas)

print("Cartas de Espadas embaralhadas:", cartas_espadas)
print("Cartas de Espadas ordenadas:", mao_ordenada)