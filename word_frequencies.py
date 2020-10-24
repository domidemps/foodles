import argparse
from collections import defaultdict
from typing import List, Tuple


def get_frequencies(sentence: str) -> defaultdict:
    """Get frequencies of words in a sentence."""

    words_list = [word for word in sentence.split(' ') if word]
    words_frequencies = defaultdict(int)
    for word in words_list:
        words_frequencies[word] += 1

    return words_frequencies


def key_function(words_frequency: Tuple[str, int]) -> Tuple[int, str]:
    """Key function for sorting."""

    return - words_frequency[1], words_frequency[0]


def sort_words_frequencies(words_frequencies: defaultdict) \
        -> List[Tuple[str, int]]:
    """Sort words frequencies pairs by decreasing frequency and
    alphabetical order."""

    return sorted(words_frequencies.items(), key=key_function)


def truncate_list(words_frequencies, n):
    """Truncate the words frequencies list given an threshold integer."""

    return words_frequencies[:n]


def get_words_frequencies(sentence: str, n: int):
    """Get the top-n words frequency of a given sentence."""

    words_frequencies = get_frequencies(sentence)
    words_frequencies_sorted = sort_words_frequencies(words_frequencies)

    return truncate_list(words_frequencies_sorted, n)


if __name__ == '__main__':

    description_msg = '''Get the top-n words frequency of a given sentence.'''

    parser = argparse.ArgumentParser(description=description_msg)
    parser.add_argument('-s', '--sentence', help='Input sentence')
    parser.add_argument('-n', '--number', help='Length of expected output')
    args = parser.parse_args()

    try:
        n = int(args.number)
        if n < 0:
            raise ValueError
    except ValueError:
        print('Invalid input - n should be a positive integer')

    print(get_words_frequencies(args.sentence, args.number))
