import pandas as pd
from scrape_single_product import scrape_single_product
from scrape_category_page import scrape_category_page
from scrape_all_categories_books import scrape_all_categories_books
from utils import save_book_to_csv
from PIL import Image
from bs4 import BeautifulSoup


menu_options = {
    1: 'For a single book',
    2: 'For all books in a single category',
    3: 'For all books in every category',
    4: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def single_book():
    book_url = input("Enter the book URL:")
    book_info = scrape_single_product(book_url)
    save_book_to_csv(book_info, "single_book")
    print('Book info has been saved!\n\n')


def one_category_books():
    category_page_url = input("Enter category page URL:")
    category_name = scrape_category_page(category_page_url)
    print(
        f'All books info from the {category_name} category have been extracted!\n\n')


def all_categories_books():
    scrape_all_categories_books()
    print('All books info from the all categories have been extracted!\n\n')


while(True):
    print("What information do you want to extract ?")
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    # Check what choice was entered and act accordingly
    if option == 1:
        single_book()
    elif option == 2:
        one_category_books()
    elif option == 3:
        all_categories_books()
    elif option == 4:
        print('Thank you for using Books To Scrape !')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
