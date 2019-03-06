#!/usr/bin/env python3

"""
Generate usernames from a corpus.
"""

import functools
import random as rd
from . import corpus


def make_name(*args):
    picked = [rd.choice(words) for words in args]
    joined = " ".join(picked)
    tidy = joined.replace("_", " ")
    caps = tidy.title()
    username = caps.replace(" ", "")
    return username


def make_description(seq_string):
    repl = (
        ("adj", "adjective"),
        ("adv", "adverb"),
        ("conj", "conjunction"),
        ("det", "determiner"),
        ("prep", "preposition")
    )
    result = functools.reduce(lambda s, r: s.replace(*r), repl, seq_string)
    return result


def make_some_names(n, verbose=False):
    abbrevs = {
        "adj-noun":      [corpus.adjectives, corpus.nouns],
        "adj-adj-noun":  [corpus.adjectives, corpus.adjectives, corpus.nouns],
        "adv-adj":       [corpus.adverbs, corpus.adjectives],
        "adv-det-noun":  [corpus.adverbs, corpus.determiners, corpus.nouns],
        "verb-prep":     [corpus.verbs, corpus.prepositions],
        "det-adj-noun":  [corpus.determiners, corpus.adjectives, corpus.nouns],
        "adj-conj-adj":  [corpus.adjectives, corpus.conjunctions,
                          corpus.adjectives],
        "verb-adv":      [corpus.verbs, corpus.adverbs],
        "verb-prep-noun": [corpus.verbs, corpus.prepositions, corpus.nouns],
        "noun-prep-noun": [corpus.nouns, corpus.prepositions, corpus.nouns],
        "noun-noun":     [corpus.nouns, corpus.nouns],
        "prep-det-noun": [corpus.prepositions, corpus.determiners,
                          corpus.nouns],
        "verb-conj-verb": [corpus.verbs, corpus.conjunctions, corpus.verbs],
        "noun-conj-noun": [corpus.nouns, corpus.conjunctions, corpus.nouns]
    }
    types = list(abbrevs.keys())
    for _ in range(n):
        selected = rd.choice(types)
        combo = abbrevs.get(selected, selected)
        info = f" ({make_description(selected)})" if verbose else ""
        print(make_name(*combo), info, sep="")
