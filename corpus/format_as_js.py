#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Combine and reformat the PoS files into one JS file.
"""

names = [
    "adjectives",
    "adverbs",
    "conjunctions",
    "determiners",
    "nouns",
    "prepositions",
    "verbs"
]


def load_list(name):
    with open(f"./{name}.txt", "r") as f:
        words = [line[:-1] for line in f]
    return words


def add_quotes(words):
    return map(lambda w: f'"{w}"', words)


def add_js_syntax(name, words):
    return f"""var {name} = [
    {", ".join(words)}
];"""


def combine_js_arrays(arrs):
    return "\n".join(arrs)


if __name__ == "__main__":
    lists = []
    for name in names:
        words = load_list(name)
        quoted = add_quotes(words)
        js_fmt = add_js_syntax(name, quoted)
        lists.append(js_fmt)
    formatted = combine_js_arrays(lists)
    with open("../lib/corpus.js", "w") as f:
        f.write(formatted)
