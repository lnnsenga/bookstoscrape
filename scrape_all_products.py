import os
from numpy import product
import pandas as pd
from scrape_single_category import scrape_single_category
from utils import request_page
from bs4 import BeautifulSoup


def scrape_all_products(url):

    category_page = request_page(url)

    soup = BeautifulSoup(category_page.content, 'html.parser')

    # all_products_urls = soup.find_all(class_='product_pod')

    all_pages_url = [url]
   
    pagination = soup.find(class_='next')

    while pagination:

        next_page_url = pagination.find('a').get('href')

        next_url = url.replace("index.html", next_page_url)
        all_pages_url.append(
            next_url
        )

        next_product_page = request_page(next_url)

        soup = BeautifulSoup(next_product_page.content, 'html.parser')

        pagination = soup.find(class_='next')



   #obtaining products from every page in a single category
    for one_page_url in all_pages_url:

        product_info = scrape_single_category(one_page_url)

    return product_info
