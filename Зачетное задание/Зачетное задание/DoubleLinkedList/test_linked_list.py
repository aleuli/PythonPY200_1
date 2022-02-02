import unittest

from task import LinkedList


class LinkedListTest(unittest.TestCase):
    def test_reversed(self):
        ll = LinkedList([1, 2, 3])

        reversed_ll = [value for value in reversed(ll)]
        self.assertEqual([3, 2, 1], reversed_ll)
