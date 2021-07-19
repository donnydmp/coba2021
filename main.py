import requests

print('Hello')
try:
    r = requests.get('https://facebook.com')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Ada error bro', e)
