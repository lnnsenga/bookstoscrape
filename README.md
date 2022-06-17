## 1. Project's Title

Books To Scrape

## 2. Project Description

A monitoring software that runs on demand via the terminal, used to extract book prices on an online book retailer named Books to Scrape.
Web address: http://books.toscrape.com/index.html

## 4. How to Install and Run the Project

1. Ensure you have the python intepreter installed on your machine
2. Download the project from Github to a directory on your computer. Github link : https://github.com/lnnsenga/bookstoscrape.git
3. Open the project folder in your IDE .( Name of the folder is _bookstoscrape_.)
4. Install the dependencies of the software by running the following code

```console
pip3 install -r requirements.txt
```

5. Run the software using the following command

```python
python bookstoscrape.py
```

**NOTE**

This software has functions that can scrape books in 3 ways

1. By extracting details for a single product from the website
2. By extracting all the products on the homepage
3. By extracting all the products on a category page

Their function call are located in the file bookstoscrape.py. They are the last lines of code in the file.
You should not call all functions at the same time. To call a particular function, ensure the other two are commented out, this is to prevent errors.

```python
# scrape_single_product()
# scrape_all_products()
scrape_category_page()
```

## When you call the function _scrape_single_product()_,

You will extract extract the following details for a single book

1. universal\_ product_code (upc)
2. title
3. price_including_tax
4. price_excluding_tax
5. number_available
6. product_description
7. category
8. review_rating
9. image_url

## When you call the function _scrape_all_products()_,

You will extract details for each book on the home page at : http://books.toscrape.com/index.html

## When you call the function _scrape_category_page()_,

You will extract book information from a single category.
If the category has more than one page, it can extract from the first page and all consecutive pages in that category.
These will be saved in the _csv_folder_ in a file that has the following format _(name of category)\category_products.csv_

**Example:** Sequential Art_category_products.csv

It will also extract images of those books, saving them in the image_folder
