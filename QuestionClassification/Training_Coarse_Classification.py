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
#import transformer

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
    st = StanfordNERTagger(read_property('StanfordNerClassifier'),
                   read_property('StanfordNerJarPath'))
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
joblib.dump(X_words, "features/x_coarse_words.pkl", compress=9) 
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

print '\n\n Try It :\n'

joblib.dump(X_POS, "features/x_coarse_POS.pkl", compress=9) 
f.close()
print ("POS feature extraction done : " +str(X_POS.shape))

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
print ("Vectorize")
joblib.dump(X_NER, "features/x_coarse_NER.pkl", compress=9) 
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
joblib.dump(X_Chunk, "features/x_coarse_Chunk.pkl", compress=9) 


X = hstack((X_words, X_POS))
X_train = hstack((X, X_NER))
X_train = hstack((X_train, X_Chunk))


######################################TESTING#############################

print ("In Testing")
#filename_test = read_property('testfilepath')
#corpus_test, test_class_gold = file_preprocess(filename_test)
corpus_test = "How many Oscas has Denzel won ? "

###words in question###

X_words = vectorizer_words.transform(corpus_test)
print ("Word features extracted : "+str(X_words.shape))


###POS tags in question###

X_POS = vectorizer_POS.transform(compute_POS_Tags(corpus_test))
print ("POS features extracted : "+str(X_POS.shape))


###NER tags in question###

X_NER = vectorizer_NER.transform(compute_NER(corpus_test))
print ("NER features extracted : "+str(X_NER.shape))


###Chunk tags in question###

X_Chunk = vectorizer_Chunk.transform(compute_Chunks(corpus_test))
print ("Chunk features extracted : "+str(X_Chunk.shape))


X = hstack((X_words, X_POS))
X_test = hstack((X, X_NER))
X_test = hstack((X_test, X_Chunk))

###################Applying the LinearSVC Classifier#########################

print ("Applying SVC")
var = LinearSVC(loss='l2', dual=False, tol=1e-3)
var = LinearSVC.fit(var, X_train, train_class)
joblib.dump(var, 'models/course_classifier.pkl', compress=9)  #saves the model into a file
print "Model Saved"

test_class = LinearSVC.predict(var, X_test)

print test_class

#####Calculating success rate#####
#hits = 0.00
#fi = open(read_property('coarse_classification_path'), "w")
#for i in range(0, len(test_class)):
#    print (test_class[i], " : ", corpus_test[i], "\n")
#    str_l = test_class[i], " : ", corpus_test[i], "\n"
#    fi.write(test_class[i] + " : ")
#    fi.write(corpus_test[i] + "\n")
#fi.close()

#for i in range(0, len(test_class)):
#    if test_class[i] == test_class_gold[i]:
#        hits = hits + 1
#print ("Number of hits = ", hits)
#print ("The accuracy is ", ((hits / len(test_class)) * 100.0), " %")
