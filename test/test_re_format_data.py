from source.re_format_data import get_seconds, get_cents, format_date, format_row

import pytest
import unittest
import warnings
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestCommon(unittest.TestCase):
    def test_get_seconds(self):
        self.assertEqual(get_seconds('0 days 0 hours 0 min 1 sec'), 1)
        self.assertEqual(get_seconds('0 days 0 hours 1 min 0 sec'), 60)
        self.assertEqual(get_seconds('0 days 1 hours 0 min 0 sec'), 3600)
        self.assertEqual(get_seconds('1 days 0 hours 0 min 0 sec'), 86400)
        self.assertEqual(get_seconds('1 days 0 hours 0 min 50 sec'), 86450)
        self.assertEqual(get_seconds('1 days 1 hours 0 min 0 sec'), 90000)
    def test_get_cents(self):
        self.assertTrue(True)
        warnings.warn("test not defined")
    def test_format_date(self):
        self.assertTrue(True)
        warnings.warn("test not defined")
    def test_format_row(self):
        self.assertTrue(True)
        warnings.warn("test not defined")

if __name__ == '__main__':
    unittest.main()