#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:25:15 2017

@author: mulang
"""
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
import re
from scipy.sparse import hstack
from sklearn.svm import LinearSVC
import nltk
from nltk.tag.stanford import StanfordNERTagger
from readproperties import read_property
from practnlptools.tools import Annotator
import os

##Compute POS##
proj_dir = os.path.abspath(os.path.join('.'))
query_proc_dir = os.path.abspath(os.path.join('QuestionClassification'))

def compute_POS_Tags(corpus):
    POS = []
    for sentence in corpus:
        text = nltk.word_tokenize(sentence)
        pos_seq = nltk.pos_tag(text)
        pos_tags = ""
        for pos in pos_seq:
            pos_tags = pos_tags + pos[1] + " "
        POS.append(pos_tags)
    return POS


##Compute NER##
def compute_NER(corpus):
    NER = []
    # fi=open("NER_features_train.txt","w")
    st = StanfordNERTagger(os.path.join(query_proc_dir,read_property('StanfordNerClassifier')),
                   os.path.join(query_proc_dir,read_property('StanfordNerJarPath')))
    for sentence in corpus:
        ner = st.tag(sentence.split())
        ner_tag = ""
        for n in ner:
            ner_tag = ner_tag + n[1] + " "
        NER.append(ner_tag)
    return NER


##Compute Chunks##
def compute_Chunks(corpus):
    Chunk_Tags = []
    annotator = Annotator()
    for sentence in corpus:
        chunks = annotator.getAnnotations(sentence)['chunk']
        chunk = ""
        for elem in chunks:
            chunk = chunk + elem[1] + " "
        # print chunk  To see what these chucks are
        Chunk_Tags.append(chunk)
    return Chunk_Tags


##removing special characters from sentence##
def preprocess(raw_sentence):
    sentence = re.sub(r'[$|.|!|"|(|)|,|;|`|\']', r'', raw_sentence)
    return sentence

f = open(os.path.join(query_proc_dir,read_property('word_features_train_coarse_path')), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_words = CountVectorizer(min_df=1)
vectorizer_words.fit_transform(corpus)
f.close()


###POS tags in question###
f = open(os.path.join(query_proc_dir,read_property('POS_features_train_coarse_path')), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_POS = CountVectorizer(min_df=1)
vectorizer_POS.fit_transform((corpus))

f = open(os.path.join(query_proc_dir,read_property('NER_features_train_coarse_path')), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_NER = CountVectorizer(min_df=1)
vectorizer_NER.fit_transform((corpus))

f = open(os.path.join(query_proc_dir,read_property('Chunk_features_train_path')), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_Chunk = CountVectorizer(min_df=1)
X_Chunk = vectorizer_Chunk.fit_transform((corpus))
f.close()

############## QUERY VECTORIZER #############################
def question_desire(question):
    this_corpus = []
    
    line = question.rstrip('\n')
    line = preprocess(line)
    sentence = ""
    words = line.split()
    for i in range(0, len(words)):
        if not(i == 0):
            sentence = sentence + (words[i]) + " "
    this_corpus.append(sentence)

    ###words in question###
    X_words = vectorizer_words.transform(this_corpus)
        
    ###POS tags in question###
    X_POS = vectorizer_POS.transform(compute_POS_Tags(this_corpus))
        
    ###NER tags in question###
    X_NER = vectorizer_NER.transform(compute_NER(this_corpus))
        
    ###Chunk tags in question###
    X_Chunk = vectorizer_Chunk.transform(compute_Chunks(this_corpus))
        
    X = hstack((X_words, X_POS))
    X_query = hstack((X, X_NER))
    X_query = hstack((X_query, X_Chunk))
    
    #print 'We here : ',query_proc_dir 
    
    clf = joblib.load(os.path.join(query_proc_dir,'models/course_classifier.pkl')) 
   
    test_class = LinearSVC.predict(clf, X_query)
    
    #print "Test Class : ", test_class

    return test_class