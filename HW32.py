pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL главной страницы
url = "http://books.toscrape.com/"

# Отправляем GET-запрос
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все книги на странице
books = soup.find_all('article', class_='product_pod')

# Проходим по всем книгам и собираем нужную информацию
for book in books:
    title = book.find('h3').find('a')['title']
    price = book.find('p', class_='price_color').text
    stock = book.find('p', class_='instock availability').text.strip()
    # Получаем относительный URL изображения
    image_url = book.find('img')['src']
    # Преобразуем в абсолютный URL
    full_image_url = urljoin(url, image_url)
    
    print(f"Название: {title}")
    print(f"Цена: {price}")
    print(f"Наличие на складе: {stock}")
    print(f"Ссылка на фото: {full_image_url}")
    print("-" * 50)



