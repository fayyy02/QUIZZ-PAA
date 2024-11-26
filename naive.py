import random

# Fungsi untuk menghasilkan bilangan random
def generate_numbers(seed, count, range_start, range_end):
    random.seed(seed)
    return [random.randint(range_start, range_end) for _ in range(count)]

# Generate 50 bilangan random
numbers = generate_numbers(seed=40, count=50, range_start=0, range_end=100)

# Fungsi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Optimisasi: hentikan jika tidak ada perubahan pada iterasi ini
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Jika tidak ada swap, array sudah terurut
        if not swapped:
            break
    return arr

# Contoh penggunaan Bubble Sort
sorted_naive = bubble_sort(numbers.copy())

# Menampilkan hasil
print("Angka asli:", numbers)
print("Hasil sorting (Naive - Bubble Sort):", sorted_naive)
