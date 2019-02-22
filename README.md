# Username Generator

A small tool to generate usernames out of existing words.

## Corpus

This uses the 50k most frequent English words from [Google Ngrams](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html).

If you'd like to use another corpus, make sure you have a separate file for each part of speech in the `corpus/` directory. The files should be named
`pos.txt`, where "*pos*" is one of: *adjectives, adverbs, conjunctions, determiners, nouns, prepositions,* and *verbs*. The files should contain one word per
line with no delimiters.

## Generating usernames

Run `usernames.py` in an interactive python session (e.g., if using IPython, enter `%run usernames.py`). This will load the list with different parts of speech
into memory. The lists will be called `adj`, `adv`, `conj`, `det`, `noun`, `prep`, and `verb`.

To generate one username, use the function `make_name()` and pass the parts of speech you want the username to have in order.

```python
In []: make_name(det, adj, noun) # Make a username with a determiner, adjective, and a noun.
Out[]: 'TheirUniversalWarrior'


In []: make_name(detm adj, adj, noun) # You can repeat parts of speech.
Out[]: 'MyExactUsefulCup'
```

To generate multiple usernames at once, use `make_some_names()` and pass it the number of names you want, and optionally a list of the sequences of parts of
speech it can choose from. If you do not pass any sequences, it will choose randomly from its pre-defined options.

Some sequences have pre-defined abbreviations. They are:
* "an": adjective, noun
* "aan": adjective, adjective, noun
* "aa": adverb, adjective
* "adn": adverb, determiner, noun
* "vp": verb, preposition
* "dan": determiner, adjective, noun
* "aca": adjective, conjunction, adjective
* "va": verb, adverb
* "vpn": verb, preposition, noun
* "npn": noun, preposition, noun
* "nn": noun, noun

Example:

```python
# Make 10 names, using all pre-defined sequences.
make_some_names(10)

# Make 5 names from the specified sequences.
make_some_names(5, ["nn", "aa", [noun, conj, noun]])
```
