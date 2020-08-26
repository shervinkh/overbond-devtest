import unittest
import os
import tempfile

import Q1
import Q2

class OverbondTest(unittest.TestCase):
    def __init__(self, *args):
        super(OverbondTest, self).__init__(*args)
        self.cleanup = []
        
    def tearDown(self):
        for path in self.cleanup:
            if os.path.exists(path):
                os.remove(path)
        
    def perform_file_test(self, component, test_name, func):
        input_file = os.path.join('tests', component, 'in_%s.csv' % test_name)
        output_file = os.path.join('tests', component, 'temp_%s.csv' % test_name)
        expected_file = os.path.join('tests', component, 'out_%s.csv' % test_name)
        self.cleanup.append(output_file)
        func(input_file, output_file)
        with open(output_file) as output, open(expected_file) as expected:
            self.assertEqual(output.read(), expected.read())

class Q1Test(OverbondTest):
    def test_readme(self):
        self.perform_file_test('Q1', 'readme', Q1.calculate_benchmarks)

    def test_sample(self):
        self.perform_file_test('Q1', 'sample', Q1.calculate_benchmarks)

    def test_split(self):
        self.perform_file_test('Q1', 'shuffle', Q1.calculate_benchmarks)
        
    def test_corner(self):
        self.perform_file_test('Q1', 'corner', Q1.calculate_benchmarks)
        
class Q2Test(OverbondTest):
    def test_readme(self):
        self.perform_file_test('Q2', 'readme', Q2.calculate_spread_to_curve)

    def test_sample(self):
        self.perform_file_test('Q2', 'sample', Q2.calculate_spread_to_curve)

    def test_split(self):
        self.perform_file_test('Q2', 'shuffle', Q2.calculate_spread_to_curve)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
