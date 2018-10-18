#!/usr/bin/env python3.6

import LeapYear
import unittest

class testStringMethods(unittest.TestCase):

    def test_true_LeapYears(self):
        self.assertTrue(LeapYear.leapYear("2000"))
        self.assertTrue(LeapYear.leapYear("0"))
        self.assertTrue(LeapYear.leapYear("1988"))
        self.assertTrue(LeapYear.leapYear("4"))
        self.assertTrue(LeapYear.leapYear("400"))
        self.assertTrue(LeapYear.leapYear("1792"))
        self.assertTrue(LeapYear.leapYear("1492"))
        self.assertTrue(LeapYear.leapYear("1600"))

    def test_false_LeapYears(self):
        self.assertFalse(LeapYear.leapYear('-3'))
        self.assertFalse(LeapYear.leapYear('1986'))
        self.assertFalse(LeapYear.leapYear('1987'))
        self.assertFalse(LeapYear.leapYear('421'))
        self.assertFalse(LeapYear.leapYear('-421'))
        self.assertFalse(LeapYear.leapYear('863'))
        self.assertFalse(LeapYear.leapYear('666'))

if __name__ == "__main__":
    unittest.main()