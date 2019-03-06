#!/usr/bin/env python3

"""
Generate usernames from a corpus.
"""

import random as rd
from . import corpus


def make_name(*args):
    picked = [rd.choice(words) for words in args]
    joined = " ".join(picked)
    tidy = joined.replace("_", " ")
    caps = tidy.title()
    username = caps.replace(" ", "")
    return username


def make_some_names(n, verbose=False):
    abbrevs = {
        "an": [corpus.adjectives, corpus.nouns],
        "aan": [corpus.adjectives, corpus.adjectives, corpus.nouns],
        "aa": [corpus.adverbs, corpus.adjectives],
        "adn": [corpus.adverbs, corpus.determiners, corpus.nouns],
        "vp": [corpus.verbs, corpus.prepositions],
        "dan": [corpus.determiners, corpus.adjectives, corpus.nouns],
        "aca": [corpus.adjectives, corpus.conjunctions, corpus.adjectives],
        "va": [corpus.verbs, corpus.adverbs],
        "vpn": [corpus.verbs, corpus.prepositions, corpus.nouns],
        "npn": [corpus.nouns, corpus.prepositions, corpus.nouns],
        "nn": [corpus.nouns, corpus.nouns],
        "pdn": [corpus.prepositions, corpus.determiners, corpus.nouns],
        "vcv": [corpus.verbs, corpus.conjunctions, corpus.verbs],
        "ncn": [corpus.nouns, corpus.conjunctions, corpus.nouns]
    }
    types = list(abbrevs.keys())
    # if not types:
    #     types = abbrevs.keys()
    for _ in range(n):
        selected = rd.choice(types)
        if verbose:
            print(selected)
        combo = abbrevs.get(selected, selected)
        print(make_name(*combo))
