#!/usr/bin/env python3

"""
Generate usernames from a corpus.
"""

import random as rd


def make_name(*args):
    picked = [rd.choice(words) for words in args]
    joined = " ".join(picked)
    tidy = joined.replace("_", " ")
    caps = tidy.title()
    username = caps.replace(" ", "")
    return username


def make_some_names(n, *args, types=None):
    adj, adv, noun, verb, det, prep, conj = args
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
