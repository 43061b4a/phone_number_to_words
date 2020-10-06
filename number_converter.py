import time
from functools import lru_cache

from trie import PrefixTree


class NumberConverter(object):

    def __init__(self):
        self.trie = PrefixTree()
        with open('words_en.txt') as file:
            lines = [line.rstrip('\n') for line in file]
            for line in lines:
                self.trie.insert(line)

    def number_to_valid_phone_words(self, num):
        if '1' in num or '0' in num:
            raise Exception('Numbers with 1 and 0 are currently not supported.')

        words = []
        for prefix in self.num_to_chars(num[0]):
            words.extend(self.trie.starts_with(prefix, len(num)))

        possible_words = []
        for word in words:
            converted_num = self.words_to_nums(word)
            if num == converted_num:
                possible_words.append(word)
        return possible_words

    @lru_cache(maxsize=10)
    def num_to_chars(self, num):
        keymap = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
        return keymap[num]

    @lru_cache(maxsize=10000)
    def words_to_nums(self, word):
        keymap = {
            'a': '2', 'b': '2', 'c': '2',
            'd': '3', 'e': '3', 'f': '3',
            'g': '4', 'h': '4', 'i': '4',
            'j': '5', 'k': '5', 'l': '5',
            'm': '6', 'n': '6', 'o': '6',
            'p': '7', 'q': '7', 'r': '7', 's': '7',
            't': '8', 'u': '8', 'v': '8',
            'w': '9', 'x': '9', 'y': '9', 'z': '9'
        }
        for char, num in keymap.items():
            word = word.replace(char, num)
        return word


converter = NumberConverter()
print('****First Run****')
for n in ['228', '888', '2382']:
    start = time.time()
    print(n, converter.number_to_valid_phone_words(n))
    end = time.time()
    print('Processing time in milliseconds:', int((end - start) * 1000))

print('****Second Run****')
for n in ['228', '888', '2382']:
    start = time.time()
    print(n, converter.number_to_valid_phone_words(n))
    end = time.time()
    print('Processing time in milliseconds:', int((end - start) * 1000))
