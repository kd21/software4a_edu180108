from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.amazon.co.jp/gp/bestsellers/books/ref=zg_bs_books_pg_1?ie=UTF8&pg=1"
browser = webdriver.PhantomJS()
browser.get(url)
browser.implicitly_wait(3)
html_source = browser.page_source
bs_obj = BeautifulSoup(html_source)
books = [a.text for a in bs_obj.select("div.a-fixed-left-grid-col div.p13n-sc-truncated")]
for b in books:
  print(b)
