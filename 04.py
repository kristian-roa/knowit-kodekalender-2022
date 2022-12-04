import numpy as np


def main():
    assert (r := solve(1000)) == 29137, f'{r} != 29137'
    print(solve(10_000_000))


def solve(n):
    return sum(multipalindrome(x) for x in range(n))


def multipalindrome(n):
    palindromes = (palindrome(n, base) for base in range(2, 17))
    count = 0
    for p in palindromes:
        if p: count += 1
        if count == 3: return n
    return 0


def palindrome(n, base):
    forwards = np.base_repr(n, base)
    backwards = forwards[::-1]

    return forwards == backwards


if __name__ == '__main__':
    main()
