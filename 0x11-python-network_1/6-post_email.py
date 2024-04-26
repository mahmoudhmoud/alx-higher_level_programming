#!/usr/bin/python3
''' sifat rssal drabit tam '''

if __name__ == '__main__':
    from sys import argv
    from requests import post
    url = argv[1]
    email = argv[2]
    res = post(url, {"email": email})
    print(res.text)
