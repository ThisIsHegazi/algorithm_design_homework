from math import sqrt

# x = []
# y = []
sum_x = sum_y = sum_x_sq = sum_y_sq = sum_xy = 0
a = b = r = 0

n = int(input("n: "))

for i in range(n):

    x_el = float(input(f"x[{i}]: "))
    # x.append(x_el)
    sum_x += x_el
    sum_x_sq += pow(x_el, 2)

    y_el = float(input(f"y[{i}]: "))
    # y.append(y_el)
    sum_y += y_el
    sum_y_sq += pow(y_el, 2)

    sum_xy += x_el * y_el


a = (n * sum_xy) - (sum_x * sum_y)
b = sqrt((n * sum_x_sq) - pow(sum_x, 2)) * sqrt((n * sum_y_sq) - pow(sum_y, 2))
try:
    r = a / b
    print(r)
except ZeroDivisionError:
    print("can't divide by zero")
