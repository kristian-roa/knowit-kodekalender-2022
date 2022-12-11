import numpy as np
from functools import reduce


def main():
    n = 4

    data = [
        0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
        0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0,
        0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0
    ]

    blocks = np.array_split(data, len(data) // n**2)

    mask = get_mask(n)
    parity_idxs = get_parity_idxs(n, mask)

    res = ''
    for block in blocks:
        decoded_block = decode(mask, parity_idxs, block)
        res += ''.join(map(str, decoded_block))

    print(res)


def get_mask(n):
    mask = np.full((n, n), 'D')
    mask[0, 0] = '-'
    mask[0, 1:-1] = 'P'
    mask[1:-1, 0] = 'P'
    return mask


def get_parity_idxs(n, mask):
    parity = []

    for i, b in enumerate(mask.flatten()):
        if b == 'P':
            parity.append((i, [e for part in np.array_split(range(n**2), n**2 // i)[1::2] for e in part]))

    return parity


def decode(mask, parity_idxs, data):
    verify = [(par_idxs, sum(data[par_idxs]) % 2 == 0) for _, par_idxs in parity_idxs]

    if not all([status for _, status in verify]):
        wrongs = reduce(np.intersect1d, [par_idxs for par_idxs, status in verify if not status])
        wrongs = reduce(np.setdiff1d, [wrongs, *[[par_idxs for par_idxs, status in verify if status]]])
        data[wrongs.squeeze()] = not data[wrongs.squeeze()]

    return data[np.argwhere(mask.flatten() == 'D').squeeze()]


if __name__ == '__main__':
    main()
