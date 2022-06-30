import os
import pandas as pd
from PIL import Image
import requests


def request_page(url):
    return requests.get(url)


def request_image(url):
    return requests.get(url, stream=True).raw


def save_to_csv(data, filename):

    print(filename)
    product_info = pd.DataFrame(data)
    f_name = filename.strip()

    # saves data to csv
    if not os.path.exists("csv_folder"):
            os.mkdir("csv_folder")
    file_name = f"csv_folder/{f_name}_category_products.csv"
    product_info.to_csv(file_name,index=False)


def save_book_to_csv(data, filename):

    product_info = pd.DataFrame(data=data)

    # saves data to csv
    if not os.path.exists("csv_folder"):
            os.mkdir("csv_folder")
    file_name = f"csv_folder/{filename.strip()}_info.csv"
    product_info.to_csv(file_name)


def save_image(image_url,title,category_name):
    img = Image.open(request_image(image_url))
    if not os.path.exists(f"image_folder/{category_name}"):
        os.mkdir(f"image_folder/{category_name}")

    img.save(f"image_folder/{category_name}/{title}_book_image.jpg")



# save_to_csv({'first name':'Lety','last name':'nk' }, "testing")