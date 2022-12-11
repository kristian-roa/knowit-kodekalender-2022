def main():
    r = 125_000
    u = 3500
    n = 10**12

    vals = {}
    for i in range(n):
        if (r, u) in vals: break
        else:
            vals[(r, u)] = i
            r, u = update(r, u)

    remainder = (n - i) % (i - vals[(r, u)])
    for _ in range(remainder): r, u = update(r, u)

    print(r)


def update(r, u):
    a = config['gamma'] * u * r
    r = int(r + (config['alpha'] * r * (config['r_max'] - r)) / config['r_max'] - a)
    u = int(u + a / config['lambda'] - config['beta'] * u)
    return r, u


if __name__ == '__main__':
    config = {
        'r_max': 10**6,
        'alpha': 0.2,
        'gamma': 7.5 * 10**-5,
        'lambda': 83,
        'beta': 0.1
    }

    main()
