import random

# Fungsi untuk menghasilkan bilangan random
def generate_numbers(seed, count, range_start, range_end):
    random.seed(seed)
    return [random.randint(range_start, range_end) for _ in range(count)]

# Generate 50 bilangan random
numbers = generate_numbers(seed=40, count=50, range_start=0, range_end=100)

# Fungsi merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

# Fungsi untuk menggabungkan dua array yang sudah terurut
def merge(left, right):
    sorted_array = []
    while left and right:
        if left[0] <= right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    sorted_array.extend(left or right)
    return sorted_array

# Contoh penggunaan:
sorted_conquer = merge_sort(numbers.copy())

# Menampilkan hasil
print("Angka asli:", numbers)
print("Hasil sorting (Conquer):", sorted_conquer)
