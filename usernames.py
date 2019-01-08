#!/usr/bin/env python3

"""
Generate usernames from WordNet.
"""

import re
import random as rd


def setup():
    # adj = load_words("adj")
    # adv = load_words("adv")
    # noun = load_words("noun")
    # verb = load_words("verb")
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
    # prefix = "/home/rachael/Documents/School/Corpora/WordNet/parsing/words/"
    # word_path = prefix + "extracted_{}.txt".format(pos)
    prefix = "/home/rachael/Documents/School/Corpora/wordfrequency_dot_info/"
    word_path = prefix + pos + ".txt"
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
        types = ["an", "aan", "aa", "va", "dan", "aca", "vp"]
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
        else:
            names.append(make_name(verb, adv))
    return names


if __name__ == "__main__":
    adj, adv, noun, verb, det, prep, conj = setup()
