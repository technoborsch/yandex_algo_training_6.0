import unittest
import psutil
import os
from time import perf_counter

from solution import can_go
from cases import cases, priority_cases, stress_case


class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_can_go(self):
        counter = 0
        for case, answer in priority_cases:
            with self.subTest(f"Priority test case {counter}, case: {case}"):
                counter += 1
                result = can_go(*case)
                self.assertEqual(answer, result)

    def test_solution(self):
        counter = 0
        for case, answer in cases:
            with self.subTest(f"Test case {counter}, case: {case}"):
                counter += 1
                n, interest_rates, useful_rates, mood = case
                result = self.solution.solve(n, interest_rates, useful_rates, mood)
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
