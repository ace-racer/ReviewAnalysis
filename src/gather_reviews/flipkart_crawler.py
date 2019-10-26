import requests
from bs4 import BeautifulSoup
import sys
import os

import utils
from template import ReviewTemplate
from review_template_filler import ReviewTemplateFiller

def get_num_pages_of_reviews(html_soup):
    num_pages = 1
    navigation_details = html_soup.find("div", class_ = "_2zg3yZ _3KSYCY")
    if navigation_details:
        num_pages_span = navigation_details.find("span")
        if num_pages_span:
            num_pages_text = num_pages_span.text
            num_pages = int(num_pages_text.replace("Page 1 of", "").strip())

    print(f"Number of pages for this product is {num_pages}")
    return num_pages

def save_reviews_for_flipkart_product(url, generated_files_base_location):
    if "reviews" not in url:
        print("The URL is not related to product reviews")
        sys.exit(1)

    generated_file_name = utils.get_product_name_from_url(url)
    generated_file_location = generated_files_base_location + generated_file_name + ".json"
    if os.path.exists(generated_file_location):
        print("Reviews already obtained for {0}".format(url))
        return generated_file_location

    flipkart_review_template_filler = ReviewTemplateFiller()
    html_parse_spec = utils.get_json_file_contents_as_dict("parse_specs/flipkart_reviews_html_parse_spec.json")

    response = requests.get(url)
    print(f"Response code: {response.status_code}")
    html_soup = BeautifulSoup(response.text, 'html.parser')

    num_pages = get_num_pages_of_reviews(html_soup)

    # Get reviews from the first page
    all_product_reviews = []

    # Get reviews from the other pages with the reviews
    current_page = 1
    while current_page <= num_pages:
        product_review_url = url + "&page=" + str(current_page)
        response = requests.get(product_review_url)
        if response.status_code == 200:
            print(f"Response code: {response.status_code}")
            html_soup = BeautifulSoup(response.text, 'html.parser')
            product_reviews = flipkart_review_template_filler.get_all_reviews_from_soup(html_soup, html_parse_spec)
            all_product_reviews.extend(product_reviews)

        current_page += 1

    print("Number of reviews retrieved")
    print(len(all_product_reviews))

    utils.create_json_file_from_dict(generated_file_location, all_product_reviews)
    return generated_file_location

if __name__ == "__main__":
    # url="https://www.flipkart.com/samsung-super-6-108cm-43-inch-ultra-hd-4k-led-smart-tv/p/itmfdzq6khv2pcvz"
    url="https://www.flipkart.com/samsung-galaxy-a70-black-128-gb/product-reviews/itmffhc79jwkwzrw?pid=MOBFFHC7GQZCF8YM"
    save_reviews_for_flipkart_product(url, "../data/reviews_received/")


