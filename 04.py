import numpy as np
import multiprocessing


def main():
    cpu = 16
    size = 10_000_000 // cpu
    jobs = [(i*size, (i+1)*size) for i in range(cpu)]

    pool = multiprocessing.Pool(cpu).map(multi_sum, jobs)
    print(sum(pool))


def multi_sum(args):
    return sum(multipalindrome(x) for x in range(args[0], args[1]))


def multipalindrome(n):
    palindromes = (palindrome(np.base_repr(n, base)) for base in range(2, 17))
    count = 0
    for p in palindromes:
        count += p
        if count == 3: return n
    return 0


def palindrome(n): return n == n[::-1]


if __name__ == '__main__':
    main()
