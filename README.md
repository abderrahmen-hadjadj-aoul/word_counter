# Word Counter

The given program counts unique words from an English text file, treating hyphen and apostrophe as part of the word. Your program must output the ten most frequent words and mention the number of occurrences.

# Usage

## Print word count report

```
> python main.py Tempest.txt
and (514)
the (513)
i (446)
to (324)
a (310)
of (295)
my (288)
you (211)
that (188)
this (185)
```

## Run tests

```
# Install pytest
pip install pytest
```

```
> pytest test.py
=============================================== test session starts ===============================================
platform linux -- Python 3.10.12, pytest-7.3.1, pluggy-1.0.0
rootdir: /home/abderrahmen/repos/word_counter
configfile: pytest.ini
plugins: cov-4.0.0, django-4.7.0, env-1.1.1, html-3.2.0, anyio-3.7.1, xdist-3.3.1, metadata-2.0.4
collected 1 item

test.py .                                                                                                   [100%]

================================================ 1 passed in 0.01s ================================================
```

## Use the library

```python

lines = [
    "Hello Bob",
    "My brother is named Bob",
    "Welcome to Texas",
]

word_counter = WordCounter()

# Lines can be any list or iterator of strings
word_counter.account_lines(lines)

# The generated report provide a list of tuple:
# [(word_1, count_1), ...]
# [("bob", "2"), ("hello", 1)]
# It will return up to the 10 most frequent words
word_stat_report = word_counter.get_stat_report()
```

**Output**

```
[('bob', 2), ('hello', 1), ('my', 1), ('brother', 1), ('is', 1), ('named', 1), ('welcome', 1), ('to', 1), ('texas', 1)]
```
