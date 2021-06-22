'''
Created to learn unit testing in python
'''

import unittest

class TestString(unittest.TestCase):

    def testStrip(self):
        name = 'aaaabbbbccccdddd'
        self.assertEqual( name.strip('ab'),'ccccdddd',"It removes all given character occurence from the actual string")

    def testSplit(self):
        name = 'a for apple, b for ball, c for cat, d for dog'
        self.assertEqual(name.split(',') , ['a for apple' ,' b for ball',' c for cat', ' d for dog'])

    def testUpper(self):
        name = 'ATISHAY'
        self.assertTrue(name.isupper(),'checks upper case string')

    def testException(self):
        with self.assertRaises(ValueError):
            int('atishay')

if __name__ == '__main__':
    unittest.main()
