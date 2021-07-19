import null as null
import requests
from bs4 import BeautifulSoup

try:
    url = requests.get('https://www.detik.com/')
    print(url.status_code)
    if url.status_code != null:
        #print(url.text)`
        print('Success')
        soup = BeautifulSoup(url.text, features='html.parser')
        print(f'Hasil Pemanggilan {url}')
        print(f'Title: {soup.title.string}')
except Exception as e:
    print('kayaknya ada yang salah deh di url')
print('Program Ended')