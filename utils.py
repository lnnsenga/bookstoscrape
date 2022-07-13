import os
import pandas as pd
from PIL import Image
import requests


def request_page(url):

    try:
        return requests.get(url)
    except Exception as e:
        print(e)

def request_image(url):
    try:
        return requests.get(url, stream=True).raw
    except Exception as e:
        print(e)

def save_to_csv(data, filename):
    product_info = pd.DataFrame(data=data)
    f_name = filename.strip()

    # saves data to csv
    if not os.path.exists("csv_folder"):
            os.mkdir("csv_folder")
    file_name = f"csv_folder/{f_name}_category_products.csv"
    product_info.to_csv(file_name,index=False)


def save_book_to_csv(data, filename):
    pd.set_option('display.max_colwidth', 20)
    product_info = pd.DataFrame(data=data)

    # saves data to csv
    if not os.path.exists("csv_folder"):
            os.mkdir("csv_folder")
    file_name = f"csv_folder/{filename.strip()}_info.csv"
    product_info.to_csv(file_name, index=False)


def save_image(image_url,title,category_name):

    img = Image.open(request_image(image_url))
    if not os.path.exists(f"image_folder/{category_name}"):   
        try:
            os.mkdir(f"image_folder/{category_name}")
        except FileNotFoundError as error:
            os.mkdir("image_folder")
            os.mkdir(f"image_folder/{category_name}")


    img.save(f"image_folder/{category_name}/{title}_book_image.jpg")
