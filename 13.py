import numpy as np


def main():
    h = 18 - 2
    r = 5

    area = np.pi * r * np.sqrt(h**2 + r**2)

    ornaments = [(4, 10), (4, 15), (2, 30), (5, 15)]
    price = sum(area * coverage / 100 * price for coverage, price in ornaments)

    print(price)


if __name__ == '__main__':
    main()
    