import pandas as pd
import requests
from bs4 import BeautifulSoup

# product_page_url
# universal_ product_code (upc)
# title
# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url


def request_page(url):
    return requests.get(url)


# def scrape_all_products():

#     data = []

#     home_page = request_page('http://books.toscrape.com/index.html')

#     soup = BeautifulSoup(home_page.content, 'html.parser')

#     all_products_urls = soup.find_all(class_='product_pod')


#     # display all books
#     for single_product_url in all_products_urls:

#         # gets the index page
#         product_page=request_page( 'http://books.toscrape.com/' + single_product_url.find('a').get('href'))

#         product = BeautifulSoup(product_page.content, 'html.parser')


#         title = product.find('h1').get_text()


#         product_description = product.find(id='product_description').find_next('p').get_text()


#         product_information = product.find_all('td')

#         universal_product_code = product_information[0].get_text()
#         price_excluding_tax = product_information[2].get_text()
#         price_including_tax = product_information[3].get_text()
#         number_available = product_information[5].get_text()


#         data.append(  {
#                 'title': [title],
#                 'universal_product_code':[ universal_product_code],
#                 'price_excluding_tax': [price_excluding_tax],
#                 'price_including_tax': [price_including_tax],
#                 'number_available': [number_available],
#                 'product_description': [product_description],
#             })


#     product_info  = pd.DataFrame(data = data)

#     # saves data to csv
#     product_info.to_csv('csv_folder/all_products_info.csv')

#     return

# .....................................................................................................

def scrape_all_products(url):

    data = []

    product_page = request_page(url)

    soup = BeautifulSoup(product_page.content, 'html.parser')

    all_products_urls = soup.find_all(class_='product_pod')

    pagination = soup.find(class_='next')

    # display all books
    for single_product_url in all_products_urls:

        # gets the index page

        new_url = single_product_url.find('a').get('href')

        complete_url = new_url.replace(
            "../../..", "http://books.toscrape.com/catalogue")

        # gets the product page
        product_page = request_page(complete_url)

        product = BeautifulSoup(product_page.content, 'html.parser')

        title = product.find('h1').get_text()

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

    return data


# ......................................................................................................

def save_to_csv(data, filename):

    product_info = pd.DataFrame(data=data)

    # saves data to csv
    file_name = f"csv_folder/{filename.strip()}_category_products.csv"
    product_info.to_csv(file_name)

# ......................................................................................................


def scrape_single_product():

    page = request_page('http://books.toscrape.com/index.html')

    soup = BeautifulSoup(page.content, 'html.parser')

    all_products_urls = soup.find_all(class_='product_pod')

    product_page = request_page(
        f"http://books.toscrape.com/{ all_products_urls[0].find('a').get('href')}")

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

    # saves data to csv
    product_info.to_csv('csv_folder/single_product_info.csv')

    return


# .....................................................................................................


def scrape_category_page():

    page = request_page('http://books.toscrape.com/index.html')

    soup = BeautifulSoup(page.content, 'html.parser')

    categories_section = soup.find(class_='side_categories')
    all_categories_urls = categories_section.find_all('a')

    category_name = all_categories_urls[2].get_text()

    # # gets the category page
    single_category_url = 'http://books.toscrape.com/' + \
        all_categories_urls[2].get('href')

    # print(single_category_url)

    category_products = scrape_all_products(single_category_url)

    # print(category_products)

    save_to_csv(category_products, category_name)

    return


# .....................................................................................................

# def scrape_image():
#     url = 'some.site.com'

#     response = requests.get(url)

#     soup = bs4.BeautifulSoup(response.text, 'html.parser')

#     image = soup.find('img')
#     image_url = image['src']


#     img = Image.open(requests.get(image_url, stream = True).raw)

#     img.save('image.jpg')


# # display all books
#     for product_page_url in all_urls:

#         # gets the index page
#         product_page=request_page( 'http://books.toscrape.com/' + product_page_url.find('a').get('href'))


#         product_page = BeautifulSoup(product_page.content, 'html.parser')

#         image = soup.find('img')
#         image_url = image['src']


#         img =


#         product_description = product.find(id='product_description').find_next('p').get_text()


#         product_information = product.find_all('td')

#         universal_product_code = product_information[0].get_text()
#         price_excluding_tax = product_information[2].get_text()
#         price_including_tax = product_information[3].get_text()
#         number_available = product_information[5].get_text()


#     return


# .....................................................................................................
# scrape_single_product()
# scrape_all_products()
scrape_category_page()