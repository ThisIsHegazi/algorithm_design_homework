# A = ½ (a + b) h
# 1. get a , b and h
# 2. add a + b as bases_sum
# 3. multiply bases_sum * h/2 as area
# 4. return area


def main():
    print(trapezoid_area(1, 1, 1))


def trapezoid_area(a: float, b: float, h: float):
    bases_sum = a + b
    area = bases_sum * h / 2
    return area


if __name__ == "__main__":
    main()
