#!/usr/bin/env python3

"""
Generate usernames from a corpus.
"""

import random as rd


def setup():
    adj = load_words("adjectives")
    adv = load_words("adverbs")
    noun = load_words("nouns")
    verb = load_words("verbs")
    det = load_words("determiners")
    prep = load_words("prepositions")
    conj = load_words("conjunctions")
    return (adj, adv, noun, verb, det, prep, conj)


def load_words(pos):
    word_path = "corpus/{}.txt".format(pos)
    with open(word_path, "r") as f:
        words = [word[:-1] for word in f]
    return words


def make_name(*args):
    picked = [rd.choice(words) for words in args]
    joined = " ".join(picked)
    tidy = joined.replace("_", " ")
    caps = tidy.title()
    username = caps.replace(" ", "")
    return username


def make_some_names(n, types=None):
    abbrevs = {
        "an": [adj, noun],
        "aan": [adj, adj, noun],
        "aa": [adv, adj],
        "adn": [adv, det, noun],
        "vp": [verb, prep],
        "dan": [det, adj, noun],
        "aca": [adj, conj, adj],
        "va": [verb, adv],
        "vpn": [verb, prep, noun],
        "npn": [noun, prep, noun],
        "nn": [noun, noun],
        "pdn": [prep, det, noun],
        "vcv": [verb, conj, verb],
        "ncn": [noun, conj, noun]
    }
    if not types:
        types = abbrevs.values()
    for _ in range(n):
        selected = rd.choice(types)
        combo = abbrevs.get(selected, selected)
        print(make_name(*combo))


if __name__ == "__main__":
    adj, adv, noun, verb, det, prep, conj = setup()
