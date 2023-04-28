import requests
from bs4 import BeautifulSoup


def get_article_links():
    links = __get_links_from_file()
    if len(links) != 0:
        return links

    return __collect_links()


def __get_links_from_file():
    with open('links.txt', 'r') as file:
        data = file.readlines()
        return data


def __collect_links():
    """
    Собыраем ссылки на новости
    """

    headers = {
        'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    host = 'https://news.google.com/'
    home_url = host + 'home'

    response = requests.get(url=home_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    articles = soup.select('article')
    with open('links.txt', 'w') as f:
        for article in articles:
            link = article.find('a')['href']
            link = host + link[1:]
            f.write(link + '\n')
            links.append(link)
        return links
