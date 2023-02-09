pimport unittest

class TestP2(unittest.TestCase):

    def test_p2(self):
        self.assertEqual(1+1, 2)
        
    def test_epic_fail(self):
        self.assertTrue(False)
