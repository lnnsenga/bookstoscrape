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

        rating = product.find(class_='star-rating')
        review_rating = rating['class']
        review_rating.remove("star-rating")
        review_rating= review_rating[0]
      

        cname = category_name[2].get_text() 
        cname = cname.strip()
        product_description = product.find(
            id='product_description').find_next('p').get_text()

        product_information = product.find_all('td')

        universal_product_code = product_information[0].get_text()
        price_excluding_tax = product_information[2].get_text()
        price_including_tax = product_information[3].get_text()
        number_available = product_information[5].get_text()
        number_available = number_available[10:12]
    
        save_image(image_url,title,cname)
        data.append({
            'title': [title],
            'universal_prod_code': [universal_product_code],
            'price_exc_tax': [price_excluding_tax],
            'price_inc_tax': [price_including_tax],
            'no_available': [number_available],
            'image_url':[image_url],
            'category':[cname],
            'r_rating':[review_rating],
            'prod_page_url':[complete_url],
            'prod_description': [product_description],    
        })

    pd.set_option('display.max_colwidth', 20)
    product_info = pd.DataFrame(data=data)

    return product_info


def scrape_single_product_(url):

  
    product_page = request_page(url)
    product_page_url =url
    data=[]
    
    product = BeautifulSoup(product_page.content, 'html.parser')

    title = product.find('h1').get_text()

    image = product.find('img')
    image_url = image['src'].replace(
            "../../", "http://books.toscrape.com/")

    rating = product.find(class_='star-rating')
    review_rating = rating['class']
    review_rating.remove("star-rating")
    review_rating= review_rating[0]
      

    category_name = product.find(class_='breadcrumb').find_all('li')
    category_name = category_name[2].get_text() 
    category_name = category_name.strip()
      

    product_description = product.find(
        id='product_description').find_next('p').get_text()

    product_information = product.find_all('td')

    universal_product_code = product_information[0].get_text()
    price_excluding_tax = product_information[2].get_text()
    price_including_tax = product_information[3].get_text()
    number_available = product_information[5].get_text()
    number_available = number_available[10:12]

    data.append({
            'title': [title],
            'universal_prod_code': [universal_product_code],
            'price_exc_tax': [price_excluding_tax],
            'price_inc_tax': [price_including_tax],
            'no_available': [number_available],
            'image_url':[image_url],
            'category':[category_name],
            'r_rating':[review_rating],
            'prod_page_url':[product_page_url],
            'prod_description': [product_description],      
    })

    pd.set_option('display.max_colwidth', 20)
    product_info = pd.DataFrame(data=data)

    return product_info
