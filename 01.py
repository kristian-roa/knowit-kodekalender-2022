import requests


def main():
    wishlist = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdkFDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--7400c6d0a99d17a53b0cdcb0b32a40026c0b44a2/letter.txt?disposition=inline').text
    dictionary = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBb1VEIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--2f6bcd547b6ffe889579dd8a1af8249693a333d7/dictionary.txt?disposition=inline').text

    translator = {a: b for a, b in (e.split(',') for e in dictionary.splitlines())}
    result = []

    while wishlist:
        for key, value in sorted(translator.items(), key=lambda k: len(k[0]), reverse=True):
            if wishlist[:len(key)] == key:
                result.append(value)
                wishlist = wishlist[len(key):]
                break

    print(len(' '.join(result)))


if __name__ == '__main__':
    main()
