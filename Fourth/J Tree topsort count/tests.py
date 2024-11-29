import unittest
import psutil
import os
from time import perf_counter

from solution import Solution
from cases import cases, stress_case


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        counter = 0
        for case, answer in cases:
            with self.subTest(f"Test case {counter}, case: {case}"):
                counter += 1
                result = self.solution.solve(*case)
                self.assertEqual(answer, result)

    def test_performance(self):
        case, answer = stress_case
        time1 = perf_counter()
        result = self.solution.solve(*case)
        time2 = perf_counter()
        print(f"Execution took {time2 - time1} sec")
        self.assertEqual(answer, result)

    def test_memory(self):
        case, answer = stress_case
        result = self.solution.solve(*case)
        process = psutil.Process(os.getpid())
        mem = process.memory_info()[0] / float(2 ** 20)
        print(f"Execution took {mem} MB")
        self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
