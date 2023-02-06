import unittest
from src.check_repo import *

class TestCheck_repo(unittest.TestCase):

    def test_check_pos(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = '5-p1-ci-feature-1-compilation'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 0)

    def test_check_neg(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = '5-p1-ci-feature-1-compilation'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 0)