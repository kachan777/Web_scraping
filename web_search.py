import requests
from bs4 import BeautifulSoup

target_url = 'https://yahoo.co.jp'  #example.co.jpは架空のドメイン。任意のurlに変更する
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for a in soup.find_all('a'):
    print(a.get('href'))         #リンクを表示
