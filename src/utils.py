import json


def get_json_file_contents_as_dict(json_file_location: str) -> dict:
    with open(json_file_location, "r") as fr:
        file_dict = json.loads(fr.read())
        return file_dict