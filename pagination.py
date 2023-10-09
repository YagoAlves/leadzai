def check_integer_input(value):
    """ checks if value is integer and return a bool"""

    return isinstance(value, int)

def check_negative_input(value):
    """ checks if the value is negative and return a bool """

    return value < 0

def generate_pagination(current_page, total_pages, boundaries, around):
    """ create a pagination using the parameters and return as string """

    result = []

    if not check_integer_input(current_page) or not check_integer_input(total_pages) or not check_integer_input(boundaries) or not check_integer_input(around):
        return "The values must be integer"

    if check_negative_input(current_page) or check_negative_input(total_pages) or check_negative_input(boundaries) or check_negative_input(around):
        return "The values must be positive"

    # Add page numbers at the beginning
    for page in range(1, min(boundaries + 1, total_pages + 1)):
        result.append(page)

    # Add ellipsis (...) if there are hidden pages between the beginning and current page
    if boundaries + 1 < current_page - around:
        result.append("...")

    # Add pages around the current page
    for page in range(max(current_page - around, boundaries + 1), min(current_page + around + 1, total_pages + 1)):
        result.append(page)

    # Add ellipsis (...) if there are hidden pages between the current page and the end
    if current_page + around < total_pages - boundaries:
        result.append("...")

    # Add page numbers at the end
    for page in range(max(total_pages - boundaries + 1, current_page + around + 1), total_pages + 1):
        result.append(page)

    # return a string
    result = " ".join(map(str,result))
    print(result)
    return result


generate_pagination(4, 5, 1, 0)