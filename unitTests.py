import unittest

from getReddit import reddit


class TestSum(unittest.TestCase):
    def test_reddit_instance(self):
        """
        Test that an instance of 'Reddit' is being established.
        This verifies the correct implementation of your environment variables.
        """
        new_reddit = reddit
        self.assertEqual(new_reddit.read_only, True)



if __name__ == '__main__':
    unittest.main()
