import requests
from collections import defaultdict
from math import ceil


def main():
    bad_acts = requests.get('https://julekalender-backend.knowit.no/challenges/2022-06/files/slemmehandlinger.txt?disposition=inline').content.decode('UTF-8')
    task = requests.get('https://julekalender-backend.knowit.no/challenges/2022-06/files/stemmer.txt?disposition=inline').content.decode('UTF-8')

    bad_acts = dict(((e := line.split(':'))[0], float(e[1])) for line in bad_acts.splitlines())
    votes = defaultdict(float)

    for line in task.splitlines():
        acts, vote = line.split(':')
        weight = min(bad_acts[act] if act in bad_acts else 1 for act in acts.split(','))
        votes[vote] += weight

    (santa, second, _) = sorted(votes.values(), reverse=True)
    print(ceil(santa - second))


if __name__ == '__main__':
    main()
