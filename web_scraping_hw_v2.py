import requests
import bs4
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'буферизация']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
base_url = 'https://habr.com'
url = base_url + '/ru/all'

response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles_for_list = soup.find_all('article')
for article_in_list in articles_for_list:
    article_link = base_url+article_in_list.find(class_="tm-article-snippet__title-link").attrs['href']
    response1 = requests.get(article_link, headers=headers)
    text1 = response1.text

    soup = bs4.BeautifulSoup(text1, features='html.parser')
    article_text = soup.find(class_='tm-article-body').text
    for word in KEYWORDS:
        if word in article_text:
            date_ = soup.find(class_='tm-article-snippet__datetime-published').next.attrs['title']
            title = soup.find('h1').find('span').text
            print(f'Статья по ключевому слову "{word}": {date_} - {title} - {article_link}')
