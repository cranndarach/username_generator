#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Format the corpus lists as a python module.
"""


def load_list(name):
    with open(f"./{name}.txt", "r") as f:
        words = [line[:-1] for line in f]
    return words


def add_quotes(words):
    return map(lambda w: f'"{w}"', words)


def add_name(name, words):
    joined = ",\n    ".join(words)
    return f"""{name} = [
    {joined}
]"""


def combine_lists(lists):
    return "\n\n".join(lists)


def main(poss, output_path):
    lists = []
    for pos in poss:
        words = load_list(pos)
        quoted = add_quotes(words)
        list_fmt = add_name(pos, quoted)
        lists.append(list_fmt)
    formatted = combine_lists(lists)
    with open(output_path, "w") as f:
        f.write(formatted)


if __name__ == "__main__":
    poss = [
        "adjectives",
        "adverbs",
        "conjunctions",
        "determiners",
        "nouns",
        "prepositions",
        "verbs"
    ]
    main(poss, "corpus.py")
