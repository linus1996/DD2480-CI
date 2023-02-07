import unittest
from src.check_repo import *

class TestCheck_repo(unittest.TestCase):

    def test_check_invalid(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = 'test-branch-missing-script'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 127)

    def test_check_pos(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = 'test-branch-compilation-success'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 0)

    def test_check_neg(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = 'test-branch-compilation-error'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 1)

    def test_check_neg2(self):
        url = 'https://github.com/linus1996/DD2480-CI.git'
        repo = 'DD2480-CI'
        branch = 'test-branch-failed-test'
        result = check(url, repo, branch)
        self.assertEqual(result.returncode, 2)