"""This module tests the functions for translating French to English and vice versa"""
import unittest
from translator import frenchToEnglish, englishToFrench

class TestF2E(unittest.TestCase): 
    def test1(self):
        """Testing French to English translation""" 
        self.assertEqual(frenchToEnglish(""), "") 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        
class TestE2F(unittest.TestCase): 
    def test1(self): 
        """Testing English to French translation""" 
        self.assertEqual(englishToFrench(""), "") 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        
unittest.main()