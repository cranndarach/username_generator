#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file for the username generator CLI.
"""

import argparse
# from username import usernames
import usernames


def setup_args():
    parser = argparse.ArgumentParser("Generate usernames from pseudo-random " +
                                     "strings of words.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print " +
                        "the parts of speech used for each username.")
    parser.add_argument("-n", help="the number of usernames to generate",
                        type=int, default=1)
    return parser.parse_args()


def init():
    adj = load_words("adjectives")
    adv = load_words("adverbs")
    noun = load_words("nouns")
    verb = load_words("verbs")
    det = load_words("determiners")
    prep = load_words("prepositions")
    conj = load_words("conjunctions")
    return (adj, adv, noun, verb, det, prep, conj)


def load_words(pos):
    word_path = "./corpus/{}.txt".format(pos)
    with open(word_path, "r") as f:
        words = [word[:-1] for word in f]
    return words


def main():
    args = setup_args()
    corpus = init()
    usernames.make_some_names(args.n, *corpus, args.verbose)


if __name__ == "__main__":
    main()
