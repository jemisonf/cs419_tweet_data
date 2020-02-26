import html
import json
import re

from stop_words import stop_words

with open("tweets.json") as f:
    words = []
    tweets = json.load(f)
    for tweet in tweets:
        # get the html unescaped, all lower case version of the tweet text
        tweet_text = html.unescape(tweet["text"]).lower()
        # remove punctuation, other garbage characters
        tweet_text = re.sub(r"[!,.?()&#…\n\t\-\+\d]", "", tweet_text)

        tweet_words = tweet_text.split(" ")

        # remove empty words
        tweet_words = list(filter(lambda word: len(word) > 0, tweet_words))
        # remove stop words
        tweet_words = list(filter(lambda word: word not in stop_words, tweet_words))

        # remove user mentions
        tweet_words = list(filter(lambda word: not re.match("@.*", word), tweet_words))

        words_string = " ".join(tweet_words)

        words.append(words_string)

    print(" ".join(words))

