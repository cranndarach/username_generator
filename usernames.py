#!/usr/bin/env python3

"""
Generate usernames from WordNet.
"""

import random as rd


def setup():
    adj = load_words("adj")
    adv = load_words("adv")
    noun = load_words("noun")
    verb = load_words("verb")
    return (adj, adv, noun, verb)


def load_words(pos):
    prefix = "/home/rachael/Documents/School/Corpora/WordNet/parsing/words/"
    word_path = prefix + "extracted_{}.txt".format(pos)
    with open(word_path, "r") as f:
        words = [word[:-1] for word in f]
    return words


def make_name(first, second):
    first_word = rd.choice(first)
    second_word = rd.choice(second)
    both = "{} {}".format(first_word, second_word)
    tidy = both.replace("_", " ")
    caps = tidy.title()
    username = caps.replace(" ", "")
    return username


def make_some_names(n, adj, adv, noun, verb):
    types = ["an", "aa", "av"]
    names = []
    for _ in range(n):
        combo = rd.choice(types)
        if combo == "an":
            names.append(make_name(adj, noun))
        elif combo == "aa":
            names.append(make_name(adv, adj))
        else:
            names.append(make_name(adv, verb))
    return names
