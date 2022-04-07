import ctypes
import os

from bs4 import BeautifulSoup
import requests
import csv

#自作PCまとめサイト速報！というサイトの記事を一括でURLを取得
res = requests.get('https://newmatosoku.com/jisakupc')

soup = BeautifulSoup(res.text, 'html.parser')
tags = soup.find("ul", class_='waku-ul')
a_tag = tags.find_all("a")

#csv形式で新規作成、書き込み
with open("link_url.csv","w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow([x['href'] for x in a_tag])
    #ファイルの保存先表示
    print(os.getcwd())






