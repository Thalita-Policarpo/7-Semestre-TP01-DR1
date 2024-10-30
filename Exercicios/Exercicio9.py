class Exercicio9:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

if __name__ == "__main__":
    exercicio = Exercicio9()
    print("Array ordenado:", exercicio.bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print("Array ordenado:", exercicio.bubble_sort([5, 40, 32, 86, 75, 91, 22]))