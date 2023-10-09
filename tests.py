import unittest
from pagination import check_integer_input, check_negative_input, generate_pagination


class TestPagination(unittest.TestCase):
    """ Test the paginate and functions used for it """

    def test_str_input(self):
        """ test check_integer_input() with a string """

        string = "value"
        assert check_integer_input(string) is False

    def test_float_input(self):
        """ test check_integer_input() with a float """

        number = 1.5
        assert check_integer_input(number) is False

    def test_negative_input(self):
        """ test check_negative_input() with a negative and positive value """

        value = 1
        assert check_negative_input(value) is False
        value = -1
        assert check_negative_input(value) is True

    def test_example_1(self):
        """ test generate_pagination() before current page """

        expected_result = "1 ... 4 5"
        current_page = 4
        total_pages = 5
        boundaries = 1
        around = 0

        result = generate_pagination(current_page, total_pages, boundaries, around)
        assert expected_result == result

    def test_example_2(self):
        """ test generate_pagination() after current page """

        expected_result = "1 2 3 4 5 6 ... 9 10"
        current_page = 4
        total_pages = 10
        boundaries = 2
        around = 2

        result = generate_pagination(current_page, total_pages, boundaries, around)
        assert expected_result == result

    def test_single_page(self):
        """ test generate_pagination() with only one page """

        expected_result = "1"
        current_page = 1
        total_pages = 1
        boundaries = 1
        around = 1

        result = generate_pagination(current_page, total_pages, boundaries, around)
        assert expected_result == result

    def test_wrong_input(self):
        """ test generate_pagination() with wrong inputs """

        expected_result = "The values must be integer"
        current_page = "1"
        total_pages = 1
        boundaries = 1
        around = 1

        result = generate_pagination(current_page, total_pages, boundaries, around)
        assert expected_result == result

        expected_result = "The values must be positive"
        current_page = -1

        result = generate_pagination(current_page, total_pages, boundaries, around)
        assert expected_result == result
