#!/usr/bin/env python3

"""
Generate usernames from a corpus.
"""

import re
import random as rd


def setup():
    adj = load_words("adjectives")
    adv = load_words("adverbs")
    noun = load_words("nouns")
    verb = load_words("verbs")
    det = load_words("determiners")
    prep = load_words("prepositions")
    conj = load_words("conjunctions")

    noun = list(filter(lambda w: not re.search(r"genus|family", w), noun))
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
    if not types:
        types = ["an", "aan", "aa", "vp", "dan", "aca", "va", "vpn", "npn", "nn"]
    names = []
    for _ in range(n):
        combo = rd.choice(types)
        if combo == "an":
            names.append(make_name(adj, noun))
        elif combo == "aan":
            names.append(make_name(adj, adj, noun))
        elif combo == "aa":
            names.append(make_name(adv, adj))
        elif combo == "vp":
            names.append(make_name(verb, prep))
        elif combo == "dan":
            names.append(make_name(det, adj, noun))
        elif combo == "aca":
            names.append(make_name(adj, conj, adj))
        elif combo == "va":
            names.append(make_name(verb, adv))
        elif combo == "vpn":
            names.append(make_name(verb, prep, noun))
        elif combo == "npn":
            names.append(make_name(noun, prep, noun))
        elif combo == "nn":
            names.append(make_name(noun, noun))
        # elif combo == "anpn":
        #     names.append(make_name(adj, noun, prep, noun))
        # elif combo == "vapn":
        #     names.append(make_name(verb, adv, prep, noun))
        else:
            names.append(make_name(*combo))
    return names


if __name__ == "__main__":
    adj, adv, noun, verb, det, prep, conj = setup()
