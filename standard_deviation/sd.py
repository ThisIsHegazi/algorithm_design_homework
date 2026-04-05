from math import sqrt

n = int(input("n=? "))
items = []
mean = 0
for i in range(n):
    value = int(input("> "))
    items.append(value)
    mean += value

print(mean)


n = len(items)
mean = mean / n

sum_of_squares = 0
for item in items:
    sum_of_squares += (item - mean) ** 2

final_result = sqrt(sum_of_squares / n)
print(final_result)
