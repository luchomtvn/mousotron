from source.data_pipeline import run_pipe

import pytest
import unittest
import warnings
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestCommon(unittest.TestCase):
    def test_run_pipe(self):
        self.assertTrue(True)
        warnings.warn("test not defined")

if __name__ == '__main__':
    unittest.main()