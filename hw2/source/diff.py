from difflib import SequenceMatcher
from typing import List, Union


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def closest_match(input_text: str, search_list: List[str], threshold=0.1) -> Union[str, None]:
    """
    Calculates closest neigbour to the input token. If nothing is look alike - returns None.

    Args: input_text: str, search_list: List[str]
    """
    max_sim = threshold
    best_guess = None

    for item in search_list:
        similarity_score = similar(input_text.lower(), item.lower())
        if similarity_score > max_sim:
            best_guess = item
            max_sim = similarity_score
    return best_guess
