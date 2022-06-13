import re

# Gensim packages
from gensim.parsing import strip_tags, strip_numeric, strip_multiple_whitespaces, strip_punctuation, preprocess_string

import spacy
from spacy.lang.nl.stop_words import STOP_WORDS



# Method does the filtering of all the unrelevant text elements
def preprocess(text):
    
    if text == None:
        return None
    
    # Custom filter method
    transform_to_lower = lambda s: s.lower()

    remove_single_char = lambda s: re.sub(r'\s+\w{1}\s+', '', s)

    # Filters to be executed in pipeline
    CLEAN_FILTERS = [strip_tags,
                strip_numeric,
                strip_punctuation, 
                strip_multiple_whitespaces, 
                transform_to_lower,
                remove_single_char]
    
    
    # Invoking gensim.parsing.preprocess_string method with set of filters
    processed_words = ' '.join(preprocess_string(text, CLEAN_FILTERS))
    
    nlp = spacy.load('nl_core_news_md')
    
    text = nlp(processed_words)
    
    pos_tags = ['ADJ', 'NOUN', 'VERB']
    
    stop_words = ['besluit', 'koninklijk', 'brussel', 'brussels', 'hoofdstedelijk', 'gewest', 'wet', 'regering', 'vlaams', 'vlaamse', 'waals', 'waalse', 'nota', 'gemeenschap', 'bevoegd', 'bevoegde', 'artikel']
    
    for i in list(STOP_WORDS):
        stop_words.append(str(i))
        
    output = []
    
    for token in text:
        if (token.pos_ in pos_tags) and (str(token) not in stop_words):
            output.append(token.lemma_)
            
    return ' '.join(output)