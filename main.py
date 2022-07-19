import requests
from bs4 import BeautifulSoup

number = 0
data = {}

def findLinksFood():
    for el in range(1):
        link = f'https://www.russianfood.com/recipes/bytype/?fid=2&page={el}#rcp_list'

        q = requests.get(link)
        result = q.content

        soup = BeautifulSoup(result, 'html.parser')

        parsingLinks = soup.findAll('div', class_='title')

        for parsingLink in parsingLinks:
           a = parsingLink.find('a')
           if a == None:
               pass
           else:
               b = 'https://www.russianfood.com' + a.get('href') + '\n'
               with open('links.txt', 'a') as file:
                   file.write(b)

def findInfoFood():
    with open('links.txt', 'r') as file:
        for line in file:
            link = line
            q = requests.get(link)
            result = q.content
            soup = BeautifulSoup(result, 'html.parser')
            getName = soup.find('h1', class_='title').text
            getInfo = soup.find('table', class_='recipe_new').find('p').text
            getIngridients = soup.find('table', class_='ingr').text.replace('\n\n','\n').replace('\n\n','\n')
            getImg = soup.find('a', class_='tozoom').get('href')
            global number
            number += 1
            print(getName + '\n', getImg + '\n', getInfo + '\n', getIngridients)

findInfoFood()