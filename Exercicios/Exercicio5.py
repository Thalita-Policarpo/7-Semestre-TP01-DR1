class Exercicio5:
    def greatest_number(self, array):
        if not array:
            return None
        max_num = array[0]
        for i in array:
            if i > max_num:
                max_num = i
        return max_num


if __name__ == "__main__":
    exercicio = Exercicio5()
    print("Maior número:", exercicio.greatest_number([1, 5, 3, 9, 2, 8]))