import unittest
from final_project.machinetranslation.translator import english_to_french, french_to_english

class TranslatorTest(unittest.TestCase):
    def test_english_to_french(self):
        french_text = english_to_french("Hello")
        self.assertEqual("Bonjour", french_text)
    
    def test_french_to_english(self):
        english_text = french_to_english("Bonjour")
        self.assertEqual("Hello", english_text)
    
    if __name__ == "__main__":
        unittest.main()


