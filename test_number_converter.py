import unittest

from number_converter import NumberConverter


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.converter = NumberConverter()

    def test_basic_functionality(self):
        result = self.converter.number_to_valid_phone_words('228')
        self.assertListEqual(result, ['abt', 'act', 'bat', 'cat'])

    def test_more_basic_functionality(self):
        result = self.converter.number_to_valid_phone_words('496')
        self.assertEqual(result, ['gym'])

    def test_singe_char(self):
        result = self.converter.number_to_valid_phone_words('2')
        self.assertEqual(result, ['a'])

    def test_long_string(self):
        result = self.converter.number_to_valid_phone_words('72384927349872938')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
