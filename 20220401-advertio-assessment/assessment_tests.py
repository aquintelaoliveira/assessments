import unittest
from assessment import print_footer_pagination

class TestAssessment(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual("1 ... 4 5", print_footer_pagination(4, 5, 1, 0))

    def test_example_2(self):
        self.assertEqual("1 2 3 4 5 6 ... 9 10", print_footer_pagination(4, 10, 2, 2))

    def test_parameters_are_not_integers(self):
        with self.assertRaises(TypeError):
            print_footer_pagination("1", "2", "3", "4")

    def test_current_page_negative_or_zero(self):
        with self.assertRaises(TypeError):
            print_footer_pagination(0, 0, 0, 0)

    def test_total_pages_negative_or_zero(self):
        with self.assertRaises(TypeError):
            print_footer_pagination(1, 0, 0, 0)

    def test_boundaries_negative(self):
        with self.assertRaises(TypeError):
            print_footer_pagination(1, 1, -1, 0)
    
    def test_around_negative(self):
        with self.assertRaises(TypeError):
            print_footer_pagination(1, 1, 0, -1)


if __name__ == '__main__':
    unittest.main()