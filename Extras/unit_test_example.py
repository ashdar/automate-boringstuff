# I'm insterested in unit testing, for the obvious reasons.
# I llke Pester, but that is PowerShell.
#
# How does Unit Testing work in Python? 
# Turns out that there is a default package for that
# This code here doesn't even start to crack the features...
# 
# This does use classes, so it's too advanced for this class and text book
# 
# .LINK
# https://docs.python.org/3/library/unittest.html

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()