from scrape_category_page import scrape_category_page_
from utils import request_page
from bs4 import BeautifulSoup

def scrape_all_categories_books():    
    category_links = []
    one_page = request_page('http://books.toscrape.com/index.html')

    soup = BeautifulSoup(one_page.content, 'html.parser')

    category_tags = soup.find(class_='side_categories').find_all('a')
    
    first_tag = category_tags[0]

    category_tags.remove(first_tag)
    

    for category_tag in category_tags:

        category_link = category_tag.get('href')
        complete_category_link = f"http://books.toscrape.com/{category_link.strip()}"


        category_links.append(
            complete_category_link
        )

    for category_link in category_links:
        scrape_category_page_(category_link)
