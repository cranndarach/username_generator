#!/usr/bin/env python3

"""
Extract word forms and separate into lists by part of speech. Save each
PoS as a separate file.
"""

import pandas as pd

input_path = "top5000.txt"

corpus = pd.read_csv(input_path, sep="\t")


def extract(pos):
    return list(set(corpus.Word.loc[corpus.Partofspeech == pos]))


def extract_and_save(pos_code, pos_string):
    words = extract(pos_code)
    with open(pos_string + ".txt", "w") as f:
        for word in words:
            f.write(word + "\n")


if __name__ == "__main__":
    extract_and_save("a", "determiners")
    extract_and_save("c", "conjunctions")
    extract_and_save("d", "quantifiers")
    extract_and_save("i", "prepositions")
    extract_and_save("j", "adjectives")
    extract_and_save("n", "nouns")
    extract_and_save("r", "adverbs")
    extract_and_save("v", "verbs")
