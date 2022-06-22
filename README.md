## 1. Project's Title

Books To Scrape

## 2. Project Description

A monitoring software that runs on demand via the terminal, used to extract book prices on an online book retailer named Books to Scrape.
Web address: http://books.toscrape.com/index.html

## 3. Before Installation
Before you installing the application, ensure you have done the following
1. Installed Python3 on your computer
2. Installed pip - the python package manager 
3. Installed the virtual environment using pip

## 4. How to Install and Run the Application

1. Open the terminal in your IDE and move to your working directory

2. Clone the application from Github to your working directory using the following command 
   ```console
      git clone https://github.com/lnnsenga/bookstoscrape.git
   ```
3. Using your terminal move from your working directory to the directory _bookstoscrape_ 

4. Create a virtual environment using the followig command 
   ```console
      virtualenv myenv
   ```

5. Activate the virtual environment using the following command
   ```console
      source myenv/bin/activate
   ```

6. Install dependencies of the project using the following command 
   ```console
      pip3 install -r requirements.txt
   ```

8. Run the application using this command 
   ```console 
      python3 scrape_category_page.py
   ```


## How The Application Works 
The final goal of the application is collection information and images for all books in a category. 
1. It starts by sending a request to the homepage of the site bookstoscrape 
2. collects the links of to all category pages 





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

1. universal product_code (upc)
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
