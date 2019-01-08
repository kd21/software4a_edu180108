from bs4 import BeautifulSoup
import requests

url = "https://www.e-hon.ne.jp/bec/SE/Genre?ccode=99&dcode=06"
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,"html.parser")

# 本のタイトルを取得
books = [a.text for a in soup.select("div.rankInner a")]
