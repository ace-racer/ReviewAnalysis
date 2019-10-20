from template import ReviewTemplate

class ReviewTemplateFiller:
    def __init__(self):
        pass

    def get_value_from_soup(self, parent_soup, html_elements_to_traverse: list):
        """
        """
        if parent_soup and html_elements_to_traverse:
            while len(html_elements_to_traverse) > 0:
                element_to_traverse = html_elements_to_traverse.pop(0)
                if element_to_traverse.get("attribute") == "class":
                    element_from_soup = parent_soup.find(element_to_traverse.get("type"), class_ = element_to_traverse.get("attribute_value"))
                    return element_from_soup
                    

        return None


    def get_all_reviews_from_soup(self, complete_soup, html_parse_spec: dict) -> list:
        """
        """
        if complete_soup and html_parse_spec:
            reviews_soup = self.get_value_from_soup(complete_soup, html_parse_spec.get("reviews_container"))
            all_extracted_reviews = []
            if reviews_soup is not None:
                for review in reviews_soup:
                    review_template = ReviewTemplate()
                    for property_name in html_parse_spec:
                        if property_name != "reviews_container":
                            property_soup = self.get_value_from_soup(review, html_parse_spec[property_name])
                            if property_soup is not None:
                                property_value = property_soup.text
                                setattr(review_template, property_name, property_value)
                        
                        all_extracted_reviews.append(review_template)

            return all_extracted_reviews





                
        

