import requests
import bs4
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'буферизация']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
base_url = 'https://habr.com'
url = base_url + '/ru/all'

response = requests.get(url, headers=headers)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    previews = article.find_all(class_='tm-article-body tm-article-snippet__lead')
    previews = [preview.text.strip() for preview in previews]
    # print(preview)
    for text in previews:
        for word in KEYWORDS:
            if word in text:
                date_ = article.find(class_='tm-article-snippet__datetime-published').next.attrs['title']
                title = article.find('h2').find('span').text
                link = base_url+article.find(class_="tm-article-snippet__title-link").attrs['href']
                print(f'Статья по ключевому слову "{word}": {date_} - {title} - {link}')
