import json
import re


def get_json_file_contents_as_dict(json_file_location: str) -> dict:
    with open(json_file_location, "r") as fr:
        file_dict = json.loads(fr.read())
        return file_dict

def create_json_file_from_dict(json_file_location: str, all_product_reviews):
    with open(json_file_location, 'w') as fp:
        json.dump(all_product_reviews, fp)

def get_product_name_from_url(reviews_url: str) -> str:
    pattern = r".com/[a-zA-Z0-9\-._]+/"
    if re.search(pattern, reviews_url):
        matched_substring = re.findall(pattern, reviews_url)[0]
        matched_substring = matched_substring.replace(".com/", "")
        matched_substring = matched_substring.replace("/", "")
        return matched_substring
    
    return None