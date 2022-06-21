import os
import pandas as pd
import requests


def request_page(url):
    return requests.get(url)


def request_image(url):
    return requests.get(url, stream=True).raw


def save_to_csv(data, filename):

    product_info = pd.DataFrame(data=data)

    # saves data to csv
    if not os.path.exists("csv_folder"):
            os.mkdir("csv_folder")
    file_name = f"csv_folder/{filename.strip()}_category_products.csv"
    product_info.to_csv(file_name)
