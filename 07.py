import requests
import numpy as np
from io import StringIO
from matplotlib import pyplot as plt


def main():
    raw = requests.get('https://julekalender-backend.knowit.no/challenges/2022-07/files/encrypted.txt?disposition=inline').text
    img = np.genfromtxt(StringIO(raw), dtype=int)

    result = np.vectorize(evil_numbers)(img)
    plt.imshow(result)
    plt.show()


def evil_numbers(n):
    return np.binary_repr(n).count('1') % 2 == 0


if __name__ == '__main__':
    main()
