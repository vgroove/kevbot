"""
The MIT License

Copyright (c) 2013 Ryan Fox

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import random
from pymongo import MongoClient

class MarkovMongo(object):
    ''' Markov Chain implementation in python with storage in MongoDB.'''

    def __init__(self, uri='mongodb://mongodb', dbname='testdb', coll='testcoll', order=2):
        connection = MongoClient(uri)
        db = connection[dbname]
        self.collection = db[coll]
        self.size = self.collection.count()
        self.order = order
        self.punctuation = ('.', '!', '?')
        self.start_word = "<<start>>"
        self.stop_word = "<<stop>>"

    def insert_file(self, filename, update=True):
        ''' Read a file and insert_words into db. '''
        with open(filename) as f:
            insert_words(f.read().split())

    def insert_words(self, words, update=True):
        ''' Read a file, parse into tuples, and insert into db.
        Be default, updates records instead of duplicating. '''
        chains = {}
        for tup in self.split(words):
            key = tuple(tup[:-1])
            if key in chains:
                chains[key].append(tup[-1])
            else:
                chains[key] = [tup[-1]]

        # Don't overwrite documents if we're updating
        if update:
            for i, key in enumerate(chains):
                    self.collection.update({'key': key}, {'$set': {'key': key, 'words': chains[key], 'i': i}}, upsert=True)
        else:
            self.collection.insert(({'i': i, 'key': key, 'words': chains[key]} for i, key in enumerate(chains)))
        self.size = self.collection.count()


    def get_words(self, key):
        ''' Get the list of words from the database corresponding to
        the supplied key.  Key should be a tuple containing two strings. '''
        result = self.collection.find_one({'key': key})
        while result == None:
            result = self.collection.find_one({'i': random.randint(0, self.size)})
        return result['words']


    def split(self, words):
        ''' Parse the supplied string into n-word chunks.  For example,
    parsing 'One small step for man' into order-3 chunks would yield:
    ('One', 'small', 'step'),
    ('small', 'step', 'for'),
    ('step', 'for', 'man')'''
        if len(words) < self.order + 1:
            return

        for i in range(len(words) - self.order):
            yield words[i : i + self.order + 1]


    def generate(self, seed=None, length=random.randint(25, 50)):
        ''' Generate text from the corpus in the database.  A seed may
    optionally be supplied.  If so, the seed should be a str, tuple, or list
    containing n strings, where n is the order of the chain. '''
        # Generate seed key
        if seed == isinstance(seed, tuple):
            row = self.collection.find_one({'key': seed})
        else:
            if seed != isinstance(seed, str):
                seed = self.start_word
            starts = self.collection.find({'key.0': seed})
            row = starts[random.randint(0, starts.count())]

        # Start constructing string, skip over start word tag
        key = row['key']
        if key[0] == self.start_word:
            words = key[1:]
        else:
            words = key[:]

        # Generate words and append to string until message length or stop word
        for i in range(length - self.order):
            newword = random.choice(self.get_words(key))
            if newword == self.stop_word:
                break
            words.append(newword)
            key.reverse()
            key.pop()
            key.reverse()
            key.append(newword)

        return ' '.join(words)

