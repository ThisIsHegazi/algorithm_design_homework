from math import pi


def main():
    print(area(10))
    print(area(20))


def area(r: float):
    a = pi * (r * r)
    return a


if __name__ == "__main__":
    main()
