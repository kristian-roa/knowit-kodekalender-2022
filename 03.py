import requests
from itertools import permutations
from math import inf
from functools import reduce

WIDTH = 110


def main():
    b = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBam9EIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--dac14d3d53d7b4014d5bb9b28c8679fd2e3ccdf9/pakker.csv?disposition=inline').text
    boxes = [map(int, box.split(',')) for box in b.splitlines()[1:]]

    result = 0

    for box in boxes:
        wraps = [sorted([width + height, 2 * (height + length)]) for height, length, width in permutations(box)]
        result += reduce(optimizer, wraps, inf)

    print(f'{result = }')


def optimizer(current, wrap):
    short, long = wrap
    if short > WIDTH: return current
    return min(current, long if long > WIDTH else short)


if __name__ == '__main__':
    main()
