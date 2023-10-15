import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontre os elementos HTML que contêm as notícias
    articles = soup.find_all('div', class_='gs-c-promo')
    
    count = 0

    for article in articles:
        if count == 10:
            break
        
        headline = article.find('h3')
        link = article.find('a', class_='gs-c-promo-heading')
        
        if headline and link:
            print("Título:", headline.text)
            print("URL:", link['href'])
            print("\n")
            count += 1
else:
    print("Falha na solicitação à página de notícias")
