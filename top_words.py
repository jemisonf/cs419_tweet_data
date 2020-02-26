from collections import Counter

with open("words") as f:
    words = f.read().split(" ")
    word_counter = Counter()
    for word in words:
        word_counter[word] += 1

    for word, count in word_counter.most_common(10):
        print(word)

