import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        time1 = data.Time(1, 20, 30)
        time2 = data.Time(2, 15, 20)
        result = lab5.time_add(time1, time2)
        expected = data.Time(3, 35, 50)
        self.assertEqual(result, expected)

    def test_time_add2(self):
        time1 = data.Time(1, 45, 50)
        time2 = data.Time(2, 30, 20)
        result = lab5.time_add(time1, time2)
        expected = data.Time(4, 16, 10)
        self.assertEqual(result, expected)

    # Part 4
    def test_is_descending1(self):
        numbers = [10.5, 9.3, 5.0, 2.1]
        self.assertTrue(lab5.is_descending(numbers))

    def test_is_descending2(self):
        numbers = [8.0, 8.0, 7.5, 6.3]
        self.assertFalse(lab5.is_descending(numbers))

    # Part 5
    def test_largest_between1(self):
        lst = [10, 20, 15, 30, 25]
        lower = 1
        upper = 3
        self.assertEqual(lab5.largest_between(lst, lower, upper), 3)

    def test_largest_between2(self):
        lst = [5, 3, 8, 12, 6]
        lower = -3
        upper = 10
        self.assertEqual(lab5.largest_between(lst, lower, upper), 3)

    # Part 6
    def test_furthest_from_origin1(self):
        points = [data.Point(1, 1), data.Point(3, 4), data.Point(-5, -6)]
        self.assertEqual(lab5.furthest_from_origin(points), 2)

    def test_furthest_from_origin2(self):
        points = []
        self.assertIsNone(lab5.furthest_from_origin(points))



if __name__ == '__main__':
    unittest.main()
