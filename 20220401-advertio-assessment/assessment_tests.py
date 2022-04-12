import unittest
from assessment import print_footer_pagination

class TestAssessment(unittest.TestCase):

    # HR examples test

    def test_example_1(self):
        self.assertEqual("1 ... 4 5", print_footer_pagination(4, 5, 1, 0))

    def test_example_2(self):
        self.assertEqual("1 2 3 4 5 6 ... 9 10", print_footer_pagination(4, 10, 2, 2))

    # Error tests

    def test_parameters_are_not_integers(self):
        with self.assertRaises(TypeError):
            print_footer_pagination("1", "2", "3", "4")

    def test_current_page_negative_or_zero(self):
        with self.assertRaises(ValueError):
            print_footer_pagination(0, 0, 0, 0)

    def test_total_pages_negative_or_zero(self):
        with self.assertRaises(ValueError):
            print_footer_pagination(1, 0, 0, 0)

    def test_boundaries_negative(self):
        with self.assertRaises(ValueError):
            print_footer_pagination(1, 1, -1, 0)
    
    def test_around_negative(self):
        with self.assertRaises(ValueError):
            print_footer_pagination(1, 1, 0, -1)

    def test_current_page_greater_than_total_pages(self):
        with self.assertRaises(ValueError):
            print_footer_pagination(10, 5, 0, 0) 

    # incrementing boundary values tests
    
    def test_incrementing_boundary_values_0(self):
        self.assertEqual("... 5 ...", print_footer_pagination(5, 10, 0, 0))

    def test_incrementing_boundary_values_1(self):
        self.assertEqual("1 ... 5 ... 10", print_footer_pagination(5, 10, 1, 0))

    def test_incrementing_boundary_values_2(self):
        self.assertEqual("1 2 ... 5 ... 9 10", print_footer_pagination(5, 10, 2, 0))

    def test_incrementing_boundary_values_3(self):
        self.assertEqual("1 2 3 ... 5 ... 8 9 10", print_footer_pagination(5, 10, 3, 0))

    def test_incrementing_boundary_values_4(self):
        self.assertEqual("1 2 3 4 5 ... 7 8 9 10",  print_footer_pagination(5, 10, 4, 0))

    def test_incrementing_boundary_values_5(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 5, 0))

    def test_incrementing_boundary_values_6(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 6, 0))

    # incrementing around values tests

    def test_incrementing_around_values_0(self):
        self.assertEqual("... 5 ...", print_footer_pagination(5, 10, 0, 0))

    def test_incrementing_around_values_1(self):
        self.assertEqual("... 4 5 6 ...", print_footer_pagination(5, 10, 0, 1))

    def test_incrementing_around_values_2(self):
        self.assertEqual("... 3 4 5 6 7 ...", print_footer_pagination(5, 10, 0, 2))

    def test_incrementing_around_values_3(self):
        self.assertEqual("... 2 3 4 5 6 7 8 ...", print_footer_pagination(5, 10, 0, 3))

    def test_incrementing_boundary_values_4(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 ...",  print_footer_pagination(5, 10, 0, 4))

    def test_incrementing_around_values_5(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 0, 5))

    def test_incrementing_around_values_6(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 0, 6))

    # incrementing both boundary around values tests

    def test_incrementing_around_values_0(self):
        self.assertEqual("... 5 ...", print_footer_pagination(5, 10, 0, 0))

    def test_incrementing_around_values_1(self):
        self.assertEqual("1 ... 4 5 6 ... 10", print_footer_pagination(5, 10, 1, 1))

    def test_incrementing_around_values_2(self):
        self.assertEqual("1 2 3 4 5 6 7 ... 9 10", print_footer_pagination(5, 10, 2, 2))

    def test_incrementing_around_values_3(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 3, 3))

    def test_incrementing_boundary_values_4(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10",  print_footer_pagination(5, 10, 4, 4))

    def test_incrementing_around_values_5(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 5, 5))

    def test_incrementing_around_values_6(self):
        self.assertEqual("1 2 3 4 5 6 7 8 9 10", print_footer_pagination(5, 10, 6, 6))

    # other edge cases
    def test_current_page_equal_to_first_page(self):    
        self.assertEqual("1 2 3 ... 8 9 10", print_footer_pagination(1, 10, 3, 1))

    def test_current_page_equal_to_last_page(self):    
        self.assertEqual("1 2 3 ... 8 9 10", print_footer_pagination(10, 10, 3, 1))

if __name__ == '__main__':
    unittest.main()