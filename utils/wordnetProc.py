#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:12:45 2017

@author: mulang
"""

from nltk.corpus import wordnet as wn

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None

def get_hypernyms(word,pos):
    try:
        word_syns = wn.synset(''+word+'.n.01')
        hypernyms = ([lemma.name() for synset in word_syns.hypernyms() for lemma in synset.lemmas()])
        return hypernyms
    except:
        pass
    return []

def get_synonyms(word,pos):
    try:
        word_syns = wn.synset(''+word+'.n.01')
        synonyms = ([lemma.name() for lemma in word_syns.lemmas()])
        return synonyms
        
    except:
        pass
    return []

def get_hyponyms(word,pos):
    try:
        word_syns = wn.synset(''+word+'.n.01')
        hyponyms = ([lemma.name() for synset in word_syns.hyponyms() for lemma in synset.lemmas()])
        return hyponyms
    except:
        pass
    return []
    

def main():
    word = "spouse"
    pos = 'n'
    
    get_synonyms(word,pos)
    print get_hyponyms(word,pos)
    print get_hypernyms(word,pos)
    
if __name__== "__main__":
  main()
