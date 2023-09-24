
import requests
from bs4 import BeautifulSoup
import json

html = requests.get('https://kun.uz/ru').text
soup = BeautifulSoup(html, 'html.parser')

block = soup.find('ul', class_='page-header__menu')
categories = block.find_all('a', class_='menu-link')

json_data = {}
for category in categories:
    category_link = 'https://kun.uz' + category.get('href')
    print(category_link)
    category_title = category.get_text()
    print(category_title)

    json_data[category_title] = []

    html = requests.get(category_link).text
    soup = BeautifulSoup(html, 'html.parser')

    block_news = soup.find('div', {'id': 'news-list'}) # {'class': 'class_name'}
    news = block_news.find_all('div', {'class': 'news'})
    print(block_news)
    for article in news:
        article_title = article.find('a', class_='news__title').get_text()
        print(article_title)
        article_link = 'https://kun.uz' + article.find('a', class_='news__title').get('href')
        print(article_link)
        article_image_link = article.find('img').get('src')
        print(article_image_link)
        article_date = article.find('div', class_='news-meta').get_text()
        print(article_date)

        json_data[category_title].append({
            'Title of the article': article_title,
            'Link to the article': article_link,
            'Link to the image': article_image_link,
            'Publication date': article_date
        })

with open('kunuz.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

