# coding: utf-8

from bs4 import BeautifulSoup
import requests

def get_score(entry):
  try:
    return entry.td.next_sibling.next_sibling.next_sibling.string
  except:
    return None

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

us = requests.get("https://ctftime.org/stats/2019/US", headers=headers).text
acad = requests.get("https://ctftime.org/stats/ac/2019", headers=headers).text
soup = BeautifulSoup(us, 'html.parser')
soup.find_all('tr')
l = soup.find_all('tr')
l = l[1:]
us = [(row.a.string, get_score(row)) for row in l]
soup = BeautifulSoup(acad, 'html.parser')
l = soup.find_all('tr')
l = l[1:]
acad = [(row.a.string, get_score(row)) for row in l]
us_acad = [team for team in acad if team in us]

rating = 0

for rank,team in zip(range(len(us_acad)),us_acad):
  print(team[0] + ": " + team[1])
  if team[0] == "Blue Hens":
    rating = rank + 1

print("\nblue hens is: " + str(rating))



