import random
from re import A

'''
Function to validate parameters values of print_footer_pagination function
'''
def validate_inputs(current_page: int, total_pages: int, boundaries: int, around: int):
    if current_page <= 0:
        raise ValueError(f"Parameter current_page can not be negative or zero")
    if total_pages <= 0:
        raise ValueError(f"Parameter total_pages can not be negative or zero") 
    if boundaries < 0:
        raise ValueError(f"Parameter boundaries can not be negative") 
    if around < 0:
        raise ValueError(f"Parameter around can not be negative")
    if current_page > total_pages:
        raise ValueError(f"Parameter current_page can not have an higher value than total_pages")

'''
Function that returns and prints to the console a pagination for a browser.

@param current_page: current page number
@param total_pages: total number of pages
@param boundaries: how many pages we want to link in the beginning, or end
@param around: how many pages we want to link before and after the current page, exclusive
@return: str with browser pagination
'''
def print_footer_pagination(current_page: int, total_pages: int, boundaries: int, around: int):

    validate_inputs(current_page, total_pages, boundaries, around)
        
    start_pages = []
    middle_pages = []
    end_pages = []

    if boundaries > 0:
         # check if boundaries and current_page values overlap
        left = boundaries if boundaries < current_page else current_page - 1
        right = total_pages - boundaries + 1 if current_page + boundaries < total_pages else current_page + 1
        start_pages = list(range(1, left + 1))
        end_pages = list(range(right, total_pages + 1))

    if around > 0:
        left = current_page - around if current_page - around >= 1 else 1
        right = current_page + around if current_page + around <= total_pages else total_pages
        # check if boundaries and around values overlap
        if boundaries > 0:
            left = left if left > start_pages[-1] else start_pages[-1] + 1
            right = right if right < end_pages[0] else end_pages[0] - 1
        middle_pages = list(range(left, right + 1))
    else:
        middle_pages.append(current_page)

    # deal with pages with no direct link
    if boundaries > 0:
        # left boundary
        if middle_pages[0] - start_pages[-1] > 1:
            middle_pages.insert(0, "...")    
        # right boundary
        if end_pages[0] - middle_pages[-1] > 1:
            middle_pages.append("...")    

    # merge all pages
    all_pages = start_pages + middle_pages + end_pages

    result = ' '.join(map(str,all_pages))
    print(result)
    return result


if __name__ == "__main__":

    print("test >> HR examples")
    print_footer_pagination(4, 5, 1, 0)
    print_footer_pagination(4, 10, 2, 2)
    print()

    print("test >> incrementing boundaries values")
    print_footer_pagination(5, 10, 0, 0)
    print_footer_pagination(5, 10, 1, 0)
    print_footer_pagination(5, 10, 2, 0)
    print_footer_pagination(5, 10, 3, 0)
    print_footer_pagination(5, 10, 4, 0)
    print_footer_pagination(5, 10, 5, 0)
    print_footer_pagination(5, 10, 6, 0)
    print()

    print("test >> incrementing around values")
    print_footer_pagination(5, 10, 0, 0)
    print_footer_pagination(5, 10, 0, 1)
    print_footer_pagination(5, 10, 0, 2)
    print_footer_pagination(5, 10, 0, 3)
    print_footer_pagination(5, 10, 0, 4)
    print_footer_pagination(5, 10, 0, 5)
    print_footer_pagination(5, 10, 0, 6)
    print()

    print("test >> incrementing both boundaries and around values")
    print_footer_pagination(5, 10, 0, 0)
    print_footer_pagination(5, 10, 1, 1)
    print_footer_pagination(5, 10, 2, 2)
    print_footer_pagination(5, 10, 3, 3)
    print_footer_pagination(5, 10, 4, 4)
    print_footer_pagination(5, 10, 5, 5)
    print_footer_pagination(5, 10, 6, 6)
    print()
