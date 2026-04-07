# binary search
def binary_search(arr: list, key: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        print("+ process happened")
        midpoint = (low + high) // 2
        if key == arr[midpoint]:
            return midpoint
        else:
            if key > arr[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint - 1
    return None


num = 1
num_ndx = binary_search([1, 2, 3, 4, 5, 500, 90000, 45645665456], num)
if num_ndx is None:
    print(f"Number {num} was not found")
else:
    print(f"Number {num} is found at index {num_ndx}")


# define low at the begining and high at the last
# get the midpoint between low and high
# if mid == key then return
# else if key > x[midpoint] then low = mid + 1 and contiune
# if key < x[midpoint] then high = mid -1 and contiune
