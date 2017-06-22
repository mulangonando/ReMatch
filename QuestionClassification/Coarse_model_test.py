#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 08:52:41 2017

@author: mulang
"""
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
#from nltk.tag.stanford import NERTagger
from nltk.tag.stanford import StanfordNERTagger
from scipy.sparse import hstack
from sklearn.svm import LinearSVC
from practnlptools.tools import Annotator
from readproperties import read_property
from sklearn.externals import joblib

##removing special characters from sentence##

def preprocess(raw_sentence):
    sentence = re.sub(r'[$|.|!|"|(|)|,|;|`|\']', r'', raw_sentence)
    return sentence

##making the file format ready to use##


def file_preprocess(filename):
    corpus = []
    classes = []
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if not (line == "\n"):
            classes.append((line.split()[0]).split(":")[0])
    for line in lines:
        line = line.rstrip('\n')
        line = preprocess(line)
        sentence = ""
        words = line.split()
        for i in range(0, len(words)):
            if not(i == 0):
                sentence = sentence + (words[i]) + " "
        corpus.append(sentence)
    f.close()
    return corpus, classes


##Compute POS##

def compute_POS_Tags(corpus):
    POS = []
    text = nltk.word_tokenize(corpus)
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
    st = StanfordNERTagger(read_property('StanfordNerClassifier'),
                   read_property('StanfordNerJarPath'))
    #for sentence in corpus:
    ner = st.tag(corpus.split())
    ner_tag = ""
    for n in ner:
        ner_tag = ner_tag + n[1] + " "
    NER.append(ner_tag)
    return NER


##Compute Chunks##

def compute_Chunks(corpus):
    Chunk_Tags = []
    annotator = Annotator()
    #for sentence in corpus:
    chunks = annotator.getAnnotations(corpus)['chunk']
    chunk = ""
    for elem in chunks:
        chunk = chunk + elem[1] + " "
    # print chunk  To see what these chucks are
    Chunk_Tags.append(chunk)
    return Chunk_Tags


######################################TRAINING############################

#######Train class labels#####

train_class = []
f = open(read_property('trainingfilepath'), 'r')
lines = f.readlines()
for line in lines:
    line = line.rstrip('\n')
    if not (line == "\n"):
        train_class.append((line.split()[0]).split(":")[0])


###words in question###

print ("Training")
f = open(read_property('word_features_train_coarse_path'), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_words = CountVectorizer(min_df=1)
X_words = vectorizer_words.fit_transform(corpus)
#joblib.dump(X_words, "features/x_coarse_words.pkl", compress=9) 
f.close()

#word_vectorizer = transformer.fit_transform(X_words)

#store the content
#with open("features/x_coarse_words.pkl", 'wb') as handle:

print ("word feature extraction done : "+str(X_words.shape))


###POS tags in question###

f = open(read_property('POS_features_train_coarse_path'), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_POS = CountVectorizer(min_df=1)
X_POS = vectorizer_POS.fit_transform((corpus))

#print '\n\n Try It :\n'

#joblib.dump(X_POS, "features/x_coarse_POS.pkl", compress=9) 
f.close()
print ("POS feature extraction done "+str(X_POS.shape))

#POS_vectorizer = transformer.fit_transform(X_POS)

#store the content
#with open("features/x_coarse_POS.pkl", 'wb') as handle:


###NER tags in question###

f = open(read_property('NER_features_train_coarse_path'), "r")
corpus = []
for lines in f:
    l = lines.split()
    words = ""
    for w in l:
        words = words + w + " "
    corpus.append(words)
vectorizer_NER = CountVectorizer(min_df=1)
X_NER = vectorizer_NER.fit_transform((corpus))
#print ("Vectorize")
#joblib.dump(X_NER, "features/x_coarse_NER.pkl", compress=9) 
f.close()
print ("NER feature extraction done : "+str(X_NER.shape))

#NER_vectorizer = transformer.fit_transform(X_NER)

#store the content
#with open("features/x_coarse_NER.pkl", 'wb') as handle:

###Chunk tags in question###

f = open(read_property('Chunk_features_train_path'), "r")
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
print ("Chunk feature extraction done : "+str(X_Chunk.shape))

#Chunks_vectorizer = transformer.fit_transform(X_Chunk)

#store the content
#with open("features/x_coarse_NER.pkl", 'wb') as handle:
#joblib.dump(X_Chunk, "features/x_coarse_Chunk.pkl", compress=9) 



######################################TESTING#############################



#vectorizer_words= CountVectorizer(min_df=1,ngram_range=(1, 2))
#vectorizer_POS= CountVectorizer(min_df=1,ngram_range=(1, 2))
#vectorizer_NER= CountVectorizer(min_df=1,ngram_range=(1, 2))
#vectorizer_Chunk= CountVectorizer(min_df=1,ngram_range=(1, 2))

#load the content
#vectorizer_words = joblib.load('features/x_coarse_words.pkl') #pickle.load(open("features/x_coarse_words.pk", "rb" ) ) 
#vectorizer_POS= joblib.load('features/x_coarse_POS.pkl')
#vectorizer_NER= joblib.load('features/x_coarse_NER.pkl')
#vectorizer_Chunk= joblib.load('features/x_coarse_Chunk.pkl')

print ("Sarting to Process the Single Query")

question = "In what city is the Heineken brewery ?"

this_corpus = []

line = question.rstrip('\n')
this_line = preprocess(line)
sentence = ""
words = this_line.split()
for i in range(0, len(words)):
    if not(i == 0):
        sentence = sentence + (words[i]) + " "
    this_corpus.append(sentence)

###words in question###
X_words = vectorizer_words.transform(this_corpus)
print 'lENGTH OF WORDS : '+ str(X_words.shape)

###POS tags in question###
computed_POS=compute_POS_Tags(this_corpus)
X_POS = vectorizer_POS.transform(computed_POS)
print 'POS : '+str(X_POS.shape)+'\n'

###NER tags in question###
computed_NER =compute_NER(this_corpus)
X_NER = vectorizer_NER.transform(computed_NER)
print 'NER : '+str(X_NER.shape)+'\n'

###Chunk tags in question###
chunks = compute_Chunks(this_corpus)
X_Chunk = vectorizer_Chunk.transform(chunks)
print 'CHUNKS : '+str(X_Chunk.shape)+'\n'

print X_words.shape, " ",X_POS.shape

X = hstack(X_words, X_POS)
X_test = hstack((X, X_NER))
X_test = hstack((X_test, X_Chunk))


###################Applying the LinearSVC Classifier#########################
clf = joblib.load('models/coarse_classifier.pkl') 
test_class = LinearSVC.predict(clf, X_test)

print "THE GIVEN QUESTION CLASS IS : "+ str(test_class)

