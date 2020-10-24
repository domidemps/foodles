import os

import unittest

from word_frequencies import get_frequencies, sort_words_frequencies, \
    truncate_list, get_words_frequencies


class TestWordFrequencies(unittest.TestCase):

    def setUp(self):

        self._test_sentence = 'foo foo bar baz bar zblah foo foo'

    def test_get_words_frequencies(self):
        # Most of the cases
        self.assertEqual(
            get_words_frequencies(
                self._test_sentence, 3), [('foo', 4), ('bar', 2), ('baz', 1)])
        # Number bigger than final list elements
        self.assertEqual(
            get_words_frequencies(self._test_sentence, 7), [('foo', 4), ('bar', 2), ('baz', 1), ('zblah', 1)])
        # Empty string as input
        self.assertEqual(get_words_frequencies('', 3), [])
        # Zero as input
        self.assertEqual(get_words_frequencies(self._test_sentence, 0), [])
        # Only spaces in the sentence
        self.assertEqual(get_words_frequencies('         ', 3), [])


if __name__ == '__main__':
    unittest.main()
