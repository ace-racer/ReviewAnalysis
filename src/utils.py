import json


def get_json_file_contents_as_dict(json_file_location: str) -> dict:
    with open(json_file_location, "r") as fr:
        file_dict = json.loads(fr.read())
        return file_dict

def create_json_file_from_dict(json_file_location: str, all_product_reviews):
    with open(json_file_location, 'w') as fp:
        json.dump(all_product_reviews, fp)