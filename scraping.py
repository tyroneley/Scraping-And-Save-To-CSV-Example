import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.serebii.net/pokedex-dp/stat/all.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = []
temp = []
counter = 0
iterator = 0
totalCount = 0

baseTable = soup.find('table', class_="dextable").find_all('td', class_="fooinfo")

for each in baseTable:
    #print(temp, iterator, totalCount)
    if totalCount == 10:
        break
    if iterator == 11:
        data.append(temp)
        temp = []
        iterator = 0
        totalCount += 1
    if (each.text.split()):
        temp.append(each.text.split())
    iterator += 1

print("Nat No. | Name | Abilities | HP Stat | Att Stat | Def Stat | S.Att Stat | S.Def Stat | Spd")
for pokemon in data:
    print(pokemon)

df = pd.DataFrame(
    {'pokemon data': data}
)

print(df.head)

df.to_csv('pokemon_data.csv', index=False)