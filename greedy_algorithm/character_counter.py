from collections import defaultdict

# counter = defaultdict(int)
# string_to_search = "alkdjflsjkfdslkfjdsakjfldsak"
# for ch in string_to_search:
#     counter[ch] += 1


# for k, v in counter.items():
#     print(f"{k} ==> {v}")
class CharFreq:
    @staticmethod
    def ascii_method(msg: str):
        print("ascii_method")
        chars = [0] * 127
        for c in msg:
            chars[ord(c)] += 1
        return chars

    @staticmethod
    def utf_method(msg: str):
        print("utf_method")
        counter = defaultdict(int)
        for c in msg:
            counter[c] += 1
        return counter


msg = "hello world"
counter = CharFreq.utf_method(msg)


arr = [[i, j] for i, j in counter.items()]


def merge_sort(arr, start, end):
    if start >= end:
        return
    middle = (start + end) // 2
    merge_sort(arr, start, middle)
    merge_sort(arr, middle + 1, end)
    merge(arr, start, middle, end)


def merge(arr, start, middle, end):
    left = arr[start : middle + 1]
    right = arr[middle + 1 : end + 1]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


print(arr)
merge_sort(arr, 0, len(arr))
print(arr)
