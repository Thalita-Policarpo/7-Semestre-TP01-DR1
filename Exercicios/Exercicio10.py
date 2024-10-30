class Exercicio10:
    def bubble_sort_strings(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

if __name__ == "__main__":
    exercicio = Exercicio10()
    print("Array ordenado:", exercicio.bubble_sort_strings(["banana", "apple", "cherry", "date"]))
    print("Array ordenado:", exercicio.bubble_sort_strings(["macaco", "cachorro", "abelha", "zebra"]))