# Username Generator

A small tool to generate usernames out of existing words.

## Corpus

### Recommended

I used the sample of the [Corpus of Contemporary American English (COCA)](https://corpus.byu.edu/coca/) from [wordfrequency.info](https://wordfrequency.info),
which you can [**download here**](https://wordfrequency.info/free.asp), and save it to `corpus/top5000.txt`. It contains the 5,000 most frequent words in the
corpus.

Then process it by running `extract_pos.py` from inside the `corpus/` folder:

```sh
$ cd corpus
$ python extract_pos.py
```

### Other corpora

If you'd like to use another corpus, make sure you have a separate file for each part of speech in the `corpus/` directory. The files should be named
`pos.txt`, where "*pos*" is one of: *adjectives, adverbs, conjunctions, determiners, nouns, prepositions, quantifiers,* and *verbs*. The files should contain
one word per line with no delimiters.
