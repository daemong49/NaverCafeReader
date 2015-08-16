# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from BeautifulSoup import BeautifulSoup
import re




driver = webdriver.Chrome('./chromedriver')

driver.get("http://static.nid.naver.com/login.nhn?svc=www1501&amp;amp;url=http%3A%2F%2Fwww.naver.com&amp;amp;t=20150513")


elem = driver.find_element_by_id("id")
elem.send_keys("hseongbae")
elem =driver.find_element_by_id("pw")
elem.send_keys("HSB49201#")
elem.submit()

time.sleep(1)

driver.get('http://cafe.naver.com/ArticleList.nhn?search.boardtype=L&search.menuid=129&search.questionTab=A&search.clubid=10338543&search.totalCount=151&search.page=1')

html = driver.page_source

print html

pattern = re.compile('<a href=\'/ArticleRead.nhn?(.*?) onclick')
matches = re.search(pattern, html)

if matches :
    leng = len(matches.group())
    print 'length:' + str(leng)

    for i in range(1, leng):
        print matches.groups(i)

driver.quit()