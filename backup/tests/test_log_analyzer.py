import unittest
from log_analyzer import analyze_log

class TestLogAnalyzer(unittest.TestCase):
    def test_sample_log(self):
        error_counter, warning_count, failed_login_count = analyze_log('sample_log.txt')
        self.assertEqual(warning_count, 2)
        self.assertEqual(failed_login_count, 3)
        self.assertGreaterEqual(len(error_counter), 1)

if __name__ == '__main__':
    unittest.main()