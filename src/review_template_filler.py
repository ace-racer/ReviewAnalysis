class ReviewTemplateFiller:
    def __init__(self):
        pass

    def get_value_from_soup(self, parent_soup, html_elements_to_traverse: list) -> str:
        if parent_soup and html_elements_to_traverse:
            while len(html_elements_to_traverse) > 0:
                element_to_traverse = html_elements_to_traverse.pop(0)
                if element_to_traverse.get("attribute") == "class":
                    element_from_soup = parent_soup.find_all(element_to_traverse.get("type"), class_ = element_to_traverse.get("attribute_value"))
                    if len(element_from_soup) > 0:
                        print(element_from_soup[0])
                    

        return None


    def get_all_reviews_from_soup(self, complete_soup, html_parse_spec: dict) -> list:
        if complete_soup and html_parse_spec:


                
        

