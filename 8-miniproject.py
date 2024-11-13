import threading

def merge(arr, left, mid, right):
    L, R = arr[left:mid + 1], arr[mid + 1:right + 1]
    i = j = 0
    for k in range(left, right + 1):
        if j >= len(R) or (i < len(L) and L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def threaded_merge_sort(arr, left, right, depth=2):
    if left < right:
        mid = (left + right) // 2
        if depth > 0:
            left_thread = threading.Thread(target=threaded_merge_sort, args=(arr, left, mid, depth - 1))
            right_thread = threading.Thread(target=threaded_merge_sort, args=(arr, mid + 1, right, depth - 1))
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()
        else:
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Main program
arr = list(map(int, input("Enter numbers to sort, separated by spaces: ").split()))
threaded_merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

