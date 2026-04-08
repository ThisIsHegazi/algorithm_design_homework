# merge sort then edit
def segregate(arr: list, start, end):
    if start >= end:
        return
    midpoint = (start + end) // 2
    segregate(arr, start, midpoint)
    segregate(arr, midpoint + 1, end)
    merge(arr, start, midpoint, end)


def merge(arr, start, mid, end):
    i = 0
    j = 0
    k = start
    left = arr[start : mid + 1]
    right = arr[mid + 1 : end + 1]
    while i < len(left) and j < len(right):
        if left[i] < 0:
            arr[k] = left[i]
            i += 1
            k += 1
        elif right[j] < 0:
            arr[k] = right[j]
            j += 1
            k += 1
        else:
            break
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


lst = [6, -5, 12, 10, -9, -1]
print(lst)
segregate(lst, 0, len(lst) - 1)
print(lst)
