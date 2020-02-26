# CS 419 (usable security) tweet analysis

This code does analysis on the data in `tweets.json`. It's tested in python 3.8 but should be compatible with other python 3 versions.

To use:
* run `python parse_tweets.py` to generate a list of all words used in the data set in a file called `words`
* run `python top_words.py` to generate a list of top ten words in the `words` file (must run `parse_tweets` first)
* run `python categories.py` to analyze three categories of tweets (see writeup for details)
