from lib import WordCounter

TEST_CASES = [
    {
        "lines": [],
        "expected_report": [],
        "error": "Should properly report empty text",
    },
    {
        "lines": ["hello"],
        "expected_report": [("hello", 1)],
        "error": "Should properly report single word text",
    },
    {
        "lines": ["hello hello hello"],
        "expected_report": [("hello", 3)],
        "error": "Should properly report single word repeated multiple times",
    },
    {
        "lines": ["hi hello hello"],
        "expected_report": [("hello", 2), ("hi", 1)],
        "error": "Should report word stats in correct order",
    },
    {
        "lines": ["hello  "],
        "expected_report": [("hello", 1)],
        "error": "Should properly account for multiple spaces",
    },
    {
        "lines": [
            "single",
            "two " * 2,
            "three " * 3,
            "four " * 4,
            "five " * 5,
            "six " * 6,
            "seven " * 7,
            "eight " * 8,
            "nine " * 9,
            "ten " * 10,
            "eleven " * 11,
        ],
        "expected_report": [
            ("eleven", 11),
            ("ten", 10),
            ("nine", 9),
            ("eight", 8),
            ("seven", 7),
            ("six", 6),
            ("five", 5),
            ("four", 4),
            ("three", 3),
            ("two", 2),
        ],
        "error": "Should report only top ten most frequent words",
    },
    {
        "lines": ["hello Hello"],
        "expected_report": [("hello", 2)],
        "error": "Should properly account for letter case",
    },
    {
        "lines": ["hello! hello."],
        "expected_report": [("hello", 2)],
        "error": "Should properly account for not letter characters",
    },
    {
        "lines": ["and and's"],
        "expected_report": [("and", 1), ("and's", 1)],
        "error": "Should properly account for apostrophes",
    },
    {
        "lines": ["flesh-fly"],
        "expected_report": [("flesh-fly", 1)],
        "error": "Should properly account for hyphen",
    },
]

def test_word_count():
    for test_case in TEST_CASES:
        assert_word_count(test_case["lines"], test_case["expected_report"], test_case["error"])

def assert_word_count(lines, expected_report, error):
    # Given
    # lines and expected_report
    # When
    word_counter = WordCounter()
    word_counter.account_lines(lines)
    word_stat_report = word_counter.get_stat_report()
    # Then
    assert word_stat_report == expected_report, error

