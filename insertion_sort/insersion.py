x = []
n = int(input("n: "))
for _ in range(n):
    x.append(int(input(f"x[{_}] ")))
print(x)


def insertion_sort(x: list) -> list:
    i = 1
    while i < n:  # n
        val = x[i]
        j = i - 1
        while j > -1:  # n
            if val < x[j]:
                x[j + 1] = x[j]
            else:
                break
            j -= 1
        x[j + 1] = val
        i += 1
    return x


# n * n +(some non important 1s) => O(n ** 2)
print(insertion_sort(x))
