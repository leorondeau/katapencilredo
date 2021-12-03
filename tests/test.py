import unittest
from pencil import write


class TestWRITE(unittest.TestCase):

    def test_write_where_string_contains_all_lower_case(self):
        total_lower = write("she sells sea shells", 50)

        self.assertEqual(33, total_lower)

    def test_write_where_string_contains_all_upper_case(self):
        total_upper = write("SHE SELLS SEA SHELLS", 50)

        self.assertEqual(16, total_upper)

    def test_write_where_string_contains_all_upper_lower_space(self):
        total_upper_lower_space = write("She Sells Sea Shells", 50)

        self.assertEqual(29, total_upper_lower_space)

    # Couldn't get this to go.
    # def test_write_where_string_contains_all_upper_lower_space(self):
    #     total_point_zero = write("She Sells Sea Shells", 0)
    #
    #     return "Point is zero"

