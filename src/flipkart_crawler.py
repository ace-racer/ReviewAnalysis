import requests
from bs4 import BeautifulSoup
import sys

import utils
from template import ReviewTemplate
from review_template_filler import ReviewTemplateFiller

# url="https://www.flipkart.com/samsung-super-6-108cm-43-inch-ultra-hd-4k-led-smart-tv/p/itmfdzq6khv2pcvz"
url="https://www.flipkart.com/samsung-super-6-138cm-55-inch-ultra-hd-4k-led-smart-tv/product-reviews/itmfdzq6xahtdzur?pid=TVSFDZQ6UPSJBGVN"



if "reviews" not in url:
    print("The URL is not related to product reviews")
    sys.exit(1)
    
response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

flipkart_review_template_filler = ReviewTemplateFiller()
html_parse_spec = utils.get_json_file_contents_as_dict("parse_specs/flipkart_reviews_html_parse_spec.json")
all_product_reviews = flipkart_review_template_filler.get_all_reviews_from_soup(html_soup, html_parse_spec)

print("Reviews")
print(all_product_reviews)

