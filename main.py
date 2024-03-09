import sys
from lib import WordCounter, print_word_stat_report


def main():
    if len(sys.argv) < 2:
        raise ValueError("Expected input file name as first argument")
    file_name = sys.argv[1]
    with open(file_name) as input_file:
        word_counter = WordCounter()
        word_counter.account_lines(input_file)
        word_stat_report = word_counter.get_stat_report()
        print_word_stat_report(word_stat_report)

if __name__ == '__main__':
    main()


lines = [
    "Hello Bob",
    "My brother is named Bob",
    "Welcome to Texas",
]

word_counter = WordCounter()
word_counter.account_lines(lines)
word_stat_report = word_counter.get_stat_report()

print(word_stat_report)
