import re
from string import punctuation
import spacy
import pandas as pd
from spacy.lang.nl import Dutch
import spacy
from heapq import nlargest
from spacy.lang.nl.stop_words import STOP_WORDS

from gensim.parsing import (
    strip_tags,
    strip_numeric,
    strip_multiple_whitespaces,
    strip_punctuation,
    preprocess_string,
)


#Calculating word frequencies from the text after removing stopwords and puntuactions:
def displayWordFrequencies(doc, stopwords):
    """
    this function returns word frequenties and should be given a doc and the stopwords corresponding to the imported language
    in spacy
    For example in Dutch:
    from spacy.lang.nl.stop_words import STOP_WORDS
    """
    nlp = loadNLP("nl")
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
def loadNLP(lang):
    """
    This function is used to load the language model from spaCy
    """
    if(lang == "nl"):
     nlp = spacy.load("nl_core_news_md")
     return nlp

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

    nlp = loadNLP("nl")

    text = nlp(processed_words)

    pos_tags = ["ADJ", "NOUN", "VERB"]

    stop_words = getStopWords()

    def delete_stopwords(input_text):
        new_text = ''
        for i in input_text.split(' '):
            if i.lower() not in stop_words:
                new_text += i + ' '
        return new_text.replace('_', '')
    
    output = []

    for token in text:
        if (token.pos_ in pos_tags):
            output.append(token.lemma_)
    
    output = " ".join(output)

    return delete_stopwords(output)

def text_analizer(doc):
    """
    This function returns tokens and lemmas from a doc
    """
    data = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_)) for token in doc]
    return data

def createDoc(my_text):
    """
    This function creates a doc from text using spaCy
    """
    nlp = loadNLP("nl")
    doc = nlp(my_text)
    return doc

def createSummary(text):
    """
    this function returns word frequenties and should be given a doc and the stopwords corresponding to the imported language
    in spacy
    For example in Dutch:
    from spacy.lang.nl.stop_words import STOP_WORDS
    """
    nlp = loadNLP("nl")
    stopwords = list(STOP_WORDS)
    doc = nlp(text)
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    #Using Maximum Frequency
    
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=(word_frequencies[word]/max_frequency)
    
    #Get sentence tokens 
    sentence_tokens= [sent for sent in doc.sents]
    #Calculate the most important sentences by adding the word frequencies in each sentence.
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                 sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                 sentence_scores[sent]+=word_frequencies[word.text.lower()]
    
    #From headhq import nlargest and calculate  30% of text with maximum score.
    select_length=int(len(sentence_tokens)*0.2)
    select_length
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    summary
    #Get the final summary of text
    final_summary=[word.text for word in summary]
    final_summary
    summary=''.join(final_summary)
    
    return summary