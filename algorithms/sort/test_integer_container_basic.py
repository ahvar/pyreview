import inspect, os, sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
from integer_container import Container
import unittest


class DemoICATest(unittest.TestCase):
    """
    This test class can be considered as a playground,
    so feel free to modify it as needed. E.g.:
     - add your own custom tests
     - delete existing tests
     - modify test content or expected output

    The results of tests from this file will always be at the beginning
    of the report generated by clicking the “Run” button.

    The results of these tests do not affect your final score
    (unless the project fails to build).
    """

    failureException = Exception

    @classmethod
    def setUp(cls):
        cls.container = Container()

    """
    Add 1, 2, 5, 4 -> [1, 2, 4, 5]
    Median of [1, 2, 4, 5] is 2
    Delete 1 -> [2, 4, 5]
    Median of [2, 4, 5] is 4
    """

    @timeout(0.1)
    def test_basic1(self):
        self.container.add(1)
        self.container.add(2)
        self.container.add(5)
        self.container.add(4)
        self.assertEqual(self.container.get_median(), 2)
        self.assertEqual(self.container.delete(1), True)
        self.assertEqual(self.container.get_median(), 4)

    """
    Add 5, 3, 5 -> [3, 5, 5]
    Median of [3, 5, 5] is 5
    Delete 5, 5, 5 -> [3]
    Median of [3] is 3
    Delete [2, 3] -> []
    Median of [] is None
    Add 1, 1, 2, 2, 2 -> [1, 1, 2, 2, 2]
    Median of [1, 1, 2, 2, 2] is 2
    Delete 2 -> [1, 1, 2, 2]
    Median of [1, 1, 2, 2] is 1
    Delete 1 -> [1, 2, 2]
    Median of [1, 2, 2] is 2
    """

    @timeout(0.1)
    def test_basic2(self):
        self.container.add(5)
        self.container.add(3)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.get_median(), 3)
        self.assertEqual(self.container.delete(2), False)
        self.assertEqual(self.container.delete(3), True)
        self.assertRaises(Exception, self.container.get_median)
        self.container.add(1)
        self.container.add(1)
        self.container.add(2)
        self.container.add(2)
        self.container.add(2)
        self.assertEqual(self.container.get_median(), 2)
        self.assertEqual(self.container.delete(2), True)
        self.assertEqual(self.container.get_median(), 1)
        self.assertEqual(self.container.delete(1), True)
        self.assertEqual(self.container.get_median(), 2)

    """
    Delete 4 -> []
    Median of [] is None
    Add 10, 9, 8, ..., 1 -> [1, 2, 3, ..., 10]
    Median of [1, 2, ..., 10] is 5
    Delete 4, 5, 6 -> [1, 2, 3, 7, 8, 9, 10]
    Median of [1, 2, 3, 7, 8, 9, 10] is 7
    """

    @timeout(0.1)
    def test_basic3(self):
        self.assertEqual(self.container.delete(4), False)
        self.assertRaises(Exception, self.container.get_median)
        for i in range(10, 0, -1):
            self.container.add(i)
        self.assertEqual(self.container.get_median(), 5)
        for i in range(4, 7):
            self.assertEqual(self.container.delete(i), True)
        self.assertEqual(self.container.get_median(), 7)
