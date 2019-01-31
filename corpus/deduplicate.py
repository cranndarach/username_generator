#!/usr/bin/env python3

"""
Remove duplicates that differ only in capitalization from lists.
"""

import sys


def deduplicate(words):
    filtered = []
    for word in words:
        if word.lower() not in filtered:
            filtered.append(word)
    return filtered


if __name__ == "__main__":
    names = [
        "pronouns"
        # "adjectives",
        # "adverbs",
        # "conjunctions",
        # "determiners",
        # "nouns",
        # "prepositions",
        # "verbs"
    ]
    for name in names:
        with open(f"{name}.txt", "r") as f:
            words = [line[:-1] for line in f]
        # print(words[:10])
        # sys.exit(0)
        filtered = deduplicate(words)
        with open(f"{name}.txt", "w") as f:
            for word in filtered:
                f.write(word)
                f.write("\n")
        filtered = []
        words = []
