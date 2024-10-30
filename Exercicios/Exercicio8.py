class Exercicio8:
    def bubble_sort_bidirectional(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            for i in range(left, right):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            right -= 1
            for i in range(right, left, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            left += 1
        return arr

if __name__ == "__main__":
    exercicio = Exercicio8()
    print("Array ordenado:", exercicio.bubble_sort_bidirectional([5, 1, 4, 2, 8]))
    print("Array ordenado:", exercicio.bubble_sort_bidirectional([9, 2, 1, 7, 6]))