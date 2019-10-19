import requests
from bs4 import BeautifulSoup
import sys

from template import ReviewTemplate

# url="https://www.flipkart.com/samsung-super-6-108cm-43-inch-ultra-hd-4k-led-smart-tv/p/itmfdzq6khv2pcvz"
url="https://www.flipkart.com/samsung-super-6-138cm-55-inch-ultra-hd-4k-led-smart-tv/product-reviews/itmfdzq6xahtdzur?pid=TVSFDZQ6UPSJBGVN"
specific_review_css_class = "col _390CkK _1gY8H-"


if "reviews" not in url:
    print("The URL is not related to product reviews")
    sys.exit(1)
    
response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

review_container = html_soup.find_all('div', class_ = '')
num_reviews_page_1 = len(review_container)
total_reviews = num_reviews_page_1

print("Number of reviews in page 1: " + str(num_reviews_page_1))

