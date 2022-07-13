from scrape_single_product import scrape_single_product
from utils import request_page,save_image
from bs4 import BeautifulSoup



def scrape_single_category(url):

    data = []
    all_products_urls = []
    one_page = request_page(url)

    soup = BeautifulSoup(one_page.content, 'html.parser')
  
    all_products = soup.find_all(class_='product_pod')

    for single_product in all_products:
        product_url = single_product.find('a').get('href')

        all_products_urls.append(
            product_url
        )

    # display all books
    for single_product_url in all_products_urls:

        complete_url = single_product_url.replace(
            "../../..", "http://books.toscrape.com/catalogue")

        single_product = scrape_single_product(complete_url)
      
        image_url = single_product[0]['image_url']
        title = single_product[0]['title']
        category = single_product[0]['category']

        save_image(image_url,title,category)
        data.append(single_product[0])


    return data