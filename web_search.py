import requests
from bs4 import BeautifulSoup

# 検索済みのリンクはタプルへ保存
visited = set()
# 検索対象の頂点となるURLを指定
q = ['https://www.yahoo.co.jp']
# URLから検索したい文字列を指定
keyword = 'guide'

# リストが空になるまでループする 
while len(q) > 0:
    url_path = q.pop(0)
    print(url_path)
    html = requests.get(url_path)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup)
    href = soup.a.get("href")
    print(href)

    # 検索したい文字列を確認
    if keyword in href:
        print(url_path)
        break

    urls = href
    for url in urls:
        if url not in visited:
            # 未検索のurlをキューへ追加する
            visited.add(url_path)
            q.append(url_path)
