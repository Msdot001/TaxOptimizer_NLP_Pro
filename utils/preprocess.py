import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from string import punctuation
import spacy
from spacy.lang.nl import Dutch
from gensim.parsing import (
    strip_tags,
    strip_numeric,
    strip_multiple_whitespaces,
    strip_punctuation,
    preprocess_string,
)

import spacy
from spacy.lang.nl.stop_words import STOP_WORDS

#Using tfidf vectorizer
def createTfidfVectorizer(df):
    """
    This function creates vectors from a given df using TfidVectorize
    """
    stopwords = getStopWords()
    tfidf_vectorizer = TfidfVectorizer(max_df=0.85, min_df=5, stop_words=stopwords)
    #tfidf = tfidf_vectorizer.fit_transform(df)
    
    return tfidf_vectorizer

#Calculating word frequencies from the text after removing stopwords and puntuactions:
def displayWordFrequencies(doc, stopwords):
    """
    this function returns word frequenties and should be given a doc and the stopwords corresponding to the imported language
    in spacy
    For example in Dutch:
    from spacy.lang.nl.stop_words import STOP_WORDS
    """
    nlp = spacy.load("nl_core_news_md")
    doc = nlp(doc)
    #First lemmatize the doc
    doc = str(" ".join([i.lemma_ for i in doc]))
    doc = nlp(doc)
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    return word_frequencies

#Calculate the maximum frequency and divide it by all frequencies to get normalized word frequencies.
def percentageImportance(word_frequencies):
    """
    This function returns the word importance percentage, we must pass word frequencie first 
    """
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=(word_frequencies[word]/max_frequency)
    
    
    return word_frequencies

def getStopWords():
    """
    This function returns the stopwords with the additional Dutch words added
    """
    stop_words = [
        "besluit",
        "koninklijk",
        "brussel",
        "brussels",
        "hoofdstedelijk",
        "gewest",
        "wet",
        "regering",
        "vlaams",
        "vlaamse",
        "waals",
        "waalse",
        "nota",
        "gemeenschap",
        "bevoegd",
        "bevoegde",
        "artikel",
    ]

    for i in list(STOP_WORDS):
        stop_words.append(str(i))

    return stop_words

def preprocess(text):

    if text == None:
        return None

    # Custom filter method
    transform_to_lower = lambda s: s.lower()

    remove_single_char = lambda s: re.sub(r"\s+\w{1}\s+", "", s)

    # Filters to be executed in pipeline
    CLEAN_FILTERS = [
        strip_tags,
        strip_numeric,
        strip_punctuation,
        strip_multiple_whitespaces,
        transform_to_lower,
        remove_single_char,
    ]

    # Invoking gensim.parsing.preprocess_string method with set of filters
    processed_words = " ".join(preprocess_string(text, CLEAN_FILTERS))

    nlp = spacy.load("nl_core_news_md")

    text = nlp(processed_words)

    pos_tags = ["ADJ", "NOUN", "VERB"]

    stop_words = getStopWords()

    output = []

    for token in text:
        if (token.pos_ in pos_tags) and (str(token) not in stop_words):
            output.append(token.lemma_.replace("_", ""))

    return " ".join(output)