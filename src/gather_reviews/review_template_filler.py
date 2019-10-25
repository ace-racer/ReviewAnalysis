from template import ReviewTemplate
from copy import deepcopy

class ReviewTemplateFiller:
    def __init__(self):
        pass

    def get_value_from_soup(self, parent_soup, html_elements_to_traverse: list, should_get_all = False):
        """
        """
        if parent_soup and html_elements_to_traverse:
            current_elements_to_traverse = html_elements_to_traverse
            itr = 0
            num_elements_to_traverse = len(current_elements_to_traverse)
            elements_from_soup = None

            # print(f"Number of elements to traverse: {num_elements_to_traverse}")
            while itr < num_elements_to_traverse:
                # print(f"ITR value {itr}")
                element_to_traverse = current_elements_to_traverse[itr]
                if element_to_traverse.get("attribute") == "class":
                    elements_from_soup = parent_soup.find_all(element_to_traverse.get("type"), class_ = element_to_traverse.get("attribute_value"))
                    if elements_from_soup:
                        if should_get_all:
                            return elements_from_soup
                        else:
                            parent_soup = elements_from_soup[0]
                            itr += 1
                    else:
                        return None
                else:
                    itr += 1

            return elements_from_soup[0]
                    
        return None


    def get_all_reviews_from_soup(self, complete_soup, html_parse_spec: dict) -> list:
        """
        """
        if complete_soup and html_parse_spec:
            reviews_soup = self.get_value_from_soup(complete_soup, html_parse_spec.get("reviews_container"), True)
            print(f"Number of reviews from reviews soup {len(reviews_soup)}")
            all_extracted_reviews = []
            if reviews_soup is not None:
                for review in reviews_soup:
                    review_template = ReviewTemplate()
                    for property_name in html_parse_spec:
                        if property_name != "reviews_container":
                            property_soup = self.get_value_from_soup(review, html_parse_spec[property_name])
                            if property_soup is not None:
                                property_value = property_soup.text
                                # print(f"Property name: {property_name} Property value: {property_value}")
                                setattr(review_template, property_name, property_value)
                        
                    all_extracted_reviews.append(review_template.__dict__)

            return all_extracted_reviews





                
        

