'''
Function to validate parameters values of print_footer_pagination function
'''
def _validate_inputs(current_page: int, total_pages: int, boundaries: int, around: int):
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
Function that adds "..." between pages with no direct link
'''
def _add_dot_dot_dot_to_between_pages_with_no_direct_link(pages: list, first_page: int, last_page: int):
    # deal with middle pages with no direct link
    i = 1
    while i < len(pages):
        if pages[i] > pages[i - 1] + 1:
            pages.insert(i, "...")
            i += 1
        i += 1

    # deal with first page with no direct link
    if pages[0] > first_page:
        pages.insert(0, "...") 
    
    # deal with last page with no direct link
    if pages[-1] < last_page:
        pages.append("...")

'''
Function that returns and prints to the console a pagination for a browser.

@param current_page: current page number
@param total_pages: total number of pages
@param boundaries: how many pages we want to link in the beginning, or end
@param around: how many pages we want to link before and after the current page, exclusive
@return: str with browser pagination
'''
def print_footer_pagination(current_page: int, total_pages: int, boundaries: int, around: int):

    _validate_inputs(current_page, total_pages, boundaries, around)
        
    left_boundary_pages = []
    around_pages = []
    right_boundary_pages = []

    if boundaries > 0:
        # left boundary
        left = boundaries if boundaries < total_pages else total_pages
        left_boundary_pages = list(range(1, left + 1))
        # right boundary
        right = total_pages - boundaries + 1 if total_pages - boundaries + 1 > 0 else 1
        right_boundary_pages = list(range(right, total_pages + 1))

    if around > 0:
        # left boundary
        left = current_page - around if current_page - around > 0 else 1
        # right boundary
        right = current_page + around if current_page + around < total_pages else total_pages
        around_pages = list(range(left, right + 1))
    else:
        around_pages.append(current_page)

    # merge all pages
    all_pages = left_boundary_pages + around_pages + right_boundary_pages
    
    # remove duplicates and sort list after
    all_pages = list( dict.fromkeys(all_pages) )
    all_pages.sort()

    # deal with pages with no direct link
    _add_dot_dot_dot_to_between_pages_with_no_direct_link(pages=all_pages, first_page=1, last_page=total_pages)

    result = ' '.join(map(str,all_pages))
    print(result)
    return result


if __name__ == "__main__":

    print("test >> HR examples")
    print_footer_pagination(current_page=4, total_pages=5, boundaries=1, around=0)
    print_footer_pagination(current_page=4, total_pages=10, boundaries=2, around=2)
    print()

    print("test >> incrementing boundaries values")
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=1, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=2, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=3, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=4, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=5, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=6, around=0)
    print()

    print("test >> incrementing around values")
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=1)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=2)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=3)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=4)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=5)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=6)
    print()

    print("test >> incrementing both boundaries and around values")
    print_footer_pagination(current_page=5, total_pages=10, boundaries=0, around=0)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=1, around=1)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=2, around=2)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=3, around=3)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=4, around=4)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=5, around=5)
    print_footer_pagination(current_page=5, total_pages=10, boundaries=6, around=6)
    print()

    print("test >> edge cases")
    print_footer_pagination(current_page=1, total_pages=10, boundaries=3, around=1)
    print_footer_pagination(current_page=10, total_pages=10, boundaries=3, around=1)
