"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):

    def test_create_counter(self):
        count1 = Counter()
        self.assertEqual(0, count1.count)
        count1.increment()
        self.assertEqual(1, count1.count)
        count1.increment()
        count1.increment()
        self.assertEqual(3, count1.count)

        # count value continue from previous counter object
        count2 = Counter()
        self.assertEqual(3, count2.count)
        count2.increment()
        self.assertEqual(4, count2.count)

