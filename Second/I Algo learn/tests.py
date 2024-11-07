import unittest
from time import perf_counter

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
                n, interest_rates, useful_rates, mood = case
                time1 = perf_counter()
                result = self.solution.solve(n, interest_rates, useful_rates, mood)
                time2 = perf_counter()
                print(f"Execution time: {time2 - time1} sec")
                self.assertEqual(answer, result)

    # def test_max(self):
    #     n = 100_000
    #     interest_rates = range(1, 100_001)
    #     useful_rates = range(1, 100_001)
    #     mood = [1] * 100_000
    #     answer = [n for n in range(1, 100_001)]
    #     time1 = perf_counter()
    #     result = self.solution.solve(n, interest_rates, useful_rates, mood)
    #     time2 = perf_counter()
    #     self.assertLess(time2 - time1, 1)
    #     self.assertEqual(result, answer)


if __name__ == "__main__":
    unittest.main()
