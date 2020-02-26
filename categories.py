from collections import Counter, defaultdict
import html
import json
import re

from stop_words import stop_words

categories = {
    "government surveillance": ("ice", "cbp", "fbi", "nsa"),
    "big tech": ("google", "facebook", "apple", "microsoft", "amazon"),
    "scams": ("win", "follow", "likert", "crypto", "winner"),
}


with open("tweets.json") as f:
    words = []
    tweets = json.load(f)
    category_counts = Counter()
    category_results = defaultdict(list)
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

        for category_name, category_words in categories.items():
            if set(category_words) & set(tweet_words):
                category_counts[category_name] += 1
                category_results[category_name].append(tweet_text)

    for category_name, category_count in category_counts.items():
        print(f"{category_name}\t\t\t{float(category_count) / float(len(tweets))}")

    for category_name, tweets in category_results.items():
        print(f"{category_name}\t\t\t{tweets[0]}")
