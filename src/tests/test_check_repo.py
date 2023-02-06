"""
import unittest
from src.check_repo import *

class TestCheck_repo(unittest.TestCase):

    def test_check_invalid(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = 'test-branch-compilation-success'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 3)
"""