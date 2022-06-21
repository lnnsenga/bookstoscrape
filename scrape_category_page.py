import os
import pandas as pd
from utils import request_page, save_to_csv
from PIL import Image
from bs4 import BeautifulSoup
from scrape_all_products import scrape_all_products


def scrape_category_page():

    page = request_page('http://books.toscrape.com/index.html')

    print("RESPONSE", page)

    soup = BeautifulSoup(page.content, 'html.parser')

    categories_section = soup.find(class_='side_categories')
    all_categories_urls = categories_section.find_all('a')

    category_name = all_categories_urls[4].get_text()

    # # gets the category page
    single_category_url = 'http://books.toscrape.com/' + \
        all_categories_urls[4].get('href')

    category_products = scrape_all_products(single_category_url)

    save_to_csv(category_products, category_name)

    return


scrape_category_page()
