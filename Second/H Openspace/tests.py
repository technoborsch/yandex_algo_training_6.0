import unittest

from solution import Solution
from cases import cases


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        counter = 0
        for case, answer in cases:
            with self.subTest(f"Test case {counter}, case: {case}"):
                counter += 1
                n, nums = case
                result = self.solution.solve(n, nums)
                self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
