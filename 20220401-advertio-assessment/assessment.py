
def validate_inputs(current_page: int, total_pages: int, boundaries: int, around: int):
    if current_page <= 0:
        raise TypeError(f"Parameter current_page can not be negative or zero")
    if total_pages <= 0:
        raise TypeError(f"Parameter total_pages can not be negative or zero") 
    if boundaries < 0:
        raise TypeError(f"Parameter boundaries can not be negative") 
    if around < 0:
        raise TypeError(f"Parameter around can not be negative")
    if current_page > total_pages:
        raise TypeError(f"Parameter current_page can not have an higher value than total_pages")


def print_footer_pagination(current_page: int, total_pages: int, boundaries: int, around: int):

    validate_inputs(current_page, total_pages, boundaries, around)
        
    start_pages = []
    middle_pages = []
    end_pages = []

    if boundaries > 0:
        start_pages = list(range(1, boundaries + 1))
        end_pages = list(range(total_pages + 1 - boundaries, total_pages + 1))

    if around > 0:
        min = current_page - around if current_page - around >= 1 else 1
        max = current_page + around + 1 if current_page + around + 1 <= total_pages else total_pages
        middle_pages = list(range(min, max))
    else:
        middle_pages.append(current_page)

    all_pages = start_pages + middle_pages + end_pages
    all_pages = list(dict.fromkeys(all_pages)) # remove duplicates

    i = 1  # deal with pages with no direct link
    while i < len(all_pages) - 1:
        if all_pages[i] > all_pages[i - 1] + 1:
            all_pages.insert(i, "...")
            i += 2
        i += 1

    result = ' '.join(map(str,all_pages))
    print(result)
    return result


if __name__ == "__main__":
    # examples
    print_footer_pagination(4, 5, 1, 0)
    print_footer_pagination(4, 10, 2, 2)
    print_footer_pagination(50, 100, 2, 10)
    print_footer_pagination(1, 100, 2, 2)
    print_footer_pagination(5, 20, 10, 20)

