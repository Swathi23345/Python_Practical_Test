import unittest
from Practical.PRACTICAL import compareStrengths


class TestcompareStrengths(unittest.TestCase):
    def testcompareStrengths1(self):
        data1 = [10]
        data2 = [5]
        result = compareStrengths(data1,data2)
        self.assertEqual(result,"RESULT: WIN")

    def testcompareStrengths2(self):
        data1 = [10]
        data2 = [10]
        result = compareStrengths(data1,data2)
        self.assertEqual(result,"Both heroes and enemies have same strengths!")

    def testcompareStrengths3(self):
        data1 = [5]
        data2 = [10]
        result = compareStrengths(data1,data2)
        self.assertEqual(result,"RESULT: LOSE")


if __name__ == '__main__':
    unittest.main()
