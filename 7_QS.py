# Write a program for analysis of quick sort by using deterministic and randomized variant
import random

def quick_sort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_deterministic(left) + middle + quick_sort_deterministic(right)

def quick_sort_randomized(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr[:pivot_index] + arr[pivot_index + 1:] if x < pivot]
    middle = [pivot]
    right = [x for x in arr[:pivot_index] + arr[pivot_index + 1:] if x > pivot]
    return quick_sort_randomized(left) + middle + quick_sort_randomized(right)

# Example usage
arr = [3, 7, 8, 5, 2, 1, 9, 6, 4]

print("Deterministic Quick Sort:")
print(quick_sort_deterministic(arr.copy()))

print("Randomized Quick Sort:")
print(quick_sort_randomized(arr.copy()))