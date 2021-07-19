import null as null
import requests

try:
    url = requests.get('https://www.instagram.com/')
    print(url.status_code)
    if url.status_code != null:
        print(url.text)
except Exception as e:
    print('kayaknya ada yang salah deh di url')
