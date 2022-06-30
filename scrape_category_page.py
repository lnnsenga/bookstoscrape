from utils import request_page, save_to_csv
from bs4 import BeautifulSoup
from scrape_all_products import scrape_all_products


def scrape_category_page_(url):

    page = request_page(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    category_name = soup.find('h1').get_text()

    category_products = scrape_all_products(url)
    print(category_products)

    save_to_csv(category_products, category_name)

    return category_name

