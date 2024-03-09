import re
from typing import Iterator

not_letter_regex = re.compile('[^a-zA-Z\'-]')


class WordCounter:

    def __init__(self):
        self.word_map = {}

    def account_lines(self, lines: Iterator[str] | list[str]):
        for line in lines:
            self._account_single_line(line)

    def get_stat_report(self):
        total_word_report = [
            (key, count) for key, count in self.word_map.items()
        ]
        total_word_report.sort(key=lambda item: item[1], reverse=True)
        return total_word_report[:10]

    def _account_single_line(self, line):
        cleaned_line = self._clean_line(line)
        words = cleaned_line.lower().split(" ")
        for word in words:
            self._account_word(word)

    def _account_word(self, word):
        if not word:
            return
        if word not in self.word_map:
            self.word_map[word] = 0
        self.word_map[word] += 1


    def _clean_line(self, line):
        return not_letter_regex.sub(' ', line)

def print_word_stat_report(report):
    for word, count in report:
        print(f"{word} ({count})")
