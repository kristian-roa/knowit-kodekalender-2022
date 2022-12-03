import requests


def main():
    gifts = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBamNEIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--3770564b85106cc053f6546adb816d383189d58b/gaver.txt?disposition=inline').content.decode('UTF-8').splitlines()

    lines = 0
    counter = 0

    for gift in gifts:
        lines += max(2, counter)
        counter += 'alv' not in gift

    print(lines)


if __name__ == '__main__':
    main()
