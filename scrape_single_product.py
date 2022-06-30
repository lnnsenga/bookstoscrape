import pandas as pd
from utils import request_page,save_image
from PIL import Image
from bs4 import BeautifulSoup


def scrape_single_product(url):

    data = []
    all_products_urls = []

    product_info = {}
    one_page = request_page(url)

    print(url)
    soup = BeautifulSoup(one_page.content, 'html.parser')

    all_products = soup.find_all(class_='product_pod')

    for single_product in all_products:
        product_url = single_product.find('a').get('href')

        all_products_urls.append(
            product_url
        )

    # display all books
    for single_product_url in all_products_urls:

        # print(single_product_url)

        complete_url = single_product_url.replace(
            "../../..", "http://books.toscrape.com/catalogue")

        # gets the product page
        product_page = request_page(complete_url)

        product = BeautifulSoup(product_page.content, 'html.parser')

        title = product.find('h1').get_text()
        category_name = product.find(class_='breadcrumb').find_all('li')
      

        if title.find("/"):
            title = title.replace("/", "-")
       

        image = product.find('img')
        image_url = image['src'].replace(
            "../../", "http://books.toscrape.com/")

        cname = category_name[2].get_text()

        save_image(image_url,title,cname.strip())
   
        product_description = product.find(
            id='product_description').find_next('p').get_text()

        product_information = product.find_all('td')

        universal_product_code = product_information[0].get_text()
        price_excluding_tax = product_information[2].get_text()
        price_including_tax = product_information[3].get_text()
        number_available = product_information[5].get_text()

        data.append({
            'title': [title],
            'universal_product_code': [universal_product_code],
            'price_excluding_tax': [price_excluding_tax],
            'price_including_tax': [price_including_tax],
            'number_available': [number_available],
            'product_description': [product_description],
        })

    product_info = pd.DataFrame(data=data)

    return product_info


def scrape_single_product_(url):

    product_page = request_page(url)

    product = BeautifulSoup(product_page.content, 'html.parser')

    title = product.find('h1').get_text()

    product_description = product.find(
        id='product_description').find_next('p').get_text()

    product_information = product.find_all('td')

    universal_product_code = product_information[0].get_text()
    price_excluding_tax = product_information[2].get_text()
    price_including_tax = product_information[3].get_text()
    number_available = product_information[5].get_text()

    product_info = pd.DataFrame(
        {
            'title': [title],
            'universal_product_code': [universal_product_code],
            'price_excluding_tax': [price_excluding_tax],
            'price_including_tax': [price_including_tax],
            'number_available': [number_available],
            'product_description': [product_description],
        }
    )


    return product_info
