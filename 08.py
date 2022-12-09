import requests
from scipy.spatial import ConvexHull

def main():
    data = requests.get('https://julekalender-backend.knowit.no/challenges/2022-08/files/data.txt?disposition=inline').text
    points = [tuple(map(int, line.split())) for line in data.splitlines()]
    area = ConvexHull(points).volume
    print(round(area))


if __name__ == '__main__':
    main()
