def merge_sort(arr, start, end):
    if start >= end:
        return
    midpoint = (end + start) // 2
    merge_sort(arr, start, midpoint)
    merge_sort(arr, midpoint + 1, end)
    merge_array(arr, start, end, midpoint)


def merge_array(arr, start, end, midpoint):
    right_arr = []
    left_arr = []
    l = start
    r = midpoint + 1
    while l <= midpoint:
        left_arr.append(arr[l])
        l += 1
    while r <= end:
        right_arr.append(arr[r])
        r += 1
    i = j = 0
    k = start
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr = [5, 4, 3, 2, 1]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
