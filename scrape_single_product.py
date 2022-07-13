from utils import request_page
from bs4 import BeautifulSoup


def scrape_single_product(url):

    product_page = request_page(url)
    product_page_url = url
    data = []

    product = BeautifulSoup(product_page.content, 'html.parser')

    title = product.find('h1').get_text()

    image = product.find('img')
    image_url = image['src'].replace(
        "../../", "http://books.toscrape.com/")

    rating = product.find(class_='star-rating')
    review_rating = rating['class']
    review_rating.remove("star-rating")
    review_rating = review_rating[0]

    category_name = product.find(class_='breadcrumb').find_all('li')
    category_name = category_name[2].get_text()
    category_name = category_name.strip()

    product_description = product.find(
        id='product_description')

    try:
        product_description = product_description.find_next('p').get_text()
    except AttributeError as error:
         product_description = '--'

    
    product_information = product.find_all('td')

    universal_product_code = product_information[0].get_text()
    price_excluding_tax = product_information[2].get_text()
    price_including_tax = product_information[3].get_text()
    number_available = product_information[5].get_text()
    number_available = number_available[10:12]

    data.append({
        'title': str(title),
        'universal_prod_code': str(universal_product_code),
        'price_exc_tax': str(price_excluding_tax),
        'price_inc_tax': str(price_including_tax),
        'no_available': str(number_available),
        'image_url': str(image_url),
        'category': str(category_name),
        'r_rating': str(review_rating),
        'prod_page_url': str(product_page_url),
        'prod_description': str(product_description),
    })

     
    return data
