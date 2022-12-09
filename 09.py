import requests
import parse
from collections import Counter


def main():
    data = requests.get('https://julekalender-backend.knowit.no/challenges/2022-09/files/julebrusmaskiner.txt?disposition=inline').text

    pattern = parse.compile('Maskin {}, temperatur {:d}C, vann {:d}L, kullsyre {:d}L')
    machines = [pattern.parse(line) for line in data.splitlines()]

    c = Counter()
    for name, temp, water, carbon in machines:
        if temp < 95 or temp > 105 or water < 400 or water > 1500 or carbon < 300 or carbon > 500: continue

        prod = water - 100 + (carbon // 10)
        if temp >= 100: prod -= prod // 40

        c[name] += prod

    print(sum(c.values()), max(c, key=c.get))


if __name__ == '__main__':
    main()
