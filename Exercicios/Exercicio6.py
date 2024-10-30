class Exercicio6:
    def quadrado_para_graos(self, graos):
        quadrado = 1
        graos_contador = 1  # Começa com 1 grão no primeiro quadrado

        while graos_contador < graos:
            quadrado += 1
            graos_contador *= 2  # Dobra a quantidade de grãos em cada quadrado

        return quadrado

if __name__ == "__main__":
    exercicio = Exercicio6()
    print("Quadrado necessário para 32 grãos:", exercicio.quadrado_para_graos(32))