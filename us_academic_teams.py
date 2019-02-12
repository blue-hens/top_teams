# coding: utf-8

from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

us = requests.get("https://ctftime.org/stats/2019/US", headers=headers).text
acad = requests.get("https://ctftime.org/stats/ac/2019", headers=headers).text
soup = BeautifulSoup(us, 'html.parser')
soup.find_all('tr')
l = soup.find_all('tr')
l = l[1:]
us = [row.a.string for row in l]
soup = BeautifulSoup(acad, 'html.parser')
l = soup.find_all('tr')
l = l[1:]
acad = [row.a.string for row in l]
us_acad = [team for team in acad if team in us]

print(us_acad)
