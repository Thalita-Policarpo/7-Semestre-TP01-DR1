class Exercicio1:
    def retornar_caracteres(self, string):
        # List comprehension para pegar cada caractere da string, exceto espaços e quebras de linha
        resultado = [char for char in string if char not in (" ", "\n")]
        return resultado

if __name__ == "__main__":
    exercicio = Exercicio1()
    print(exercicio.retornar_caracteres("Sítio do pica-pau amarelo \n 2023"))