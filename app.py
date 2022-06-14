from utils.preprocess import preprocess
from utils.preprocess import displayWordFrequencies
from utils.preprocess import percentageImportance
from utils.preprocess import getStopWords
from venv import create
import streamlit as st
from streamlit_lottie import st_lottie

from spacy import displacy
import json
import requests
import spacy

#Change default name of app on Browser Tab
st.set_page_config(page_title='TextOptimizer App', layout="wide")
st.title("Text Optimizer NLP App")
st.subheader("Choose your NLP Solution and Enter your Text:")

def main():
    """
    This main function is called to execute the code to run the app
    """
    #Ref:https://blog.jcharistech.com/2019/11/28/summarizer-and-named-entity-checker-app-with-streamlit-and-spacy/
    HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
    col1, col2 = st.columns([1,3])


    #Adding animation
    lottie_animation = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_nxbn4wl8.json")

    with st.container():
        with col1:
            st_lottie(lottie_animation,
                height=384,
                width=384)
        with col2:
    #Tokenatization

            if st.checkbox("Show Tokens and Lemma"):
                st.subheader("Tokenize Text")
                message = st.text_area("Enter your Text", "Type Here")
            #For now just to test:
                if st.button("Analyze"):
                    nlp_result = text_analizer(createDoc(message))
                    st.json(nlp_result)
    #Named Entity 
            if st.checkbox("Name Entity Recognition"):
                st.subheader("Extract Entities")
                message = st.text_area("Enter your Text", "Type Here")
                
                if st.button("Recognize"):
                        doc = createDoc(message)
                        html = displacy.render(doc,style="ent")
                        html = html.replace("\n\n","\n")
                        st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)
    #Word Importance                    
            if st.checkbox("Word Importance"):
                st.subheader("Show word importance in Text")
                message = st.text_area("Enter your Text", "Type Here")
                stopwords = getStopWords()
                if st.button("Analyze"):
                        doc = preprocess(message)
                        word_frequencie = displayWordFrequencies(doc, stopwords)
                        pImportance = percentageImportance(word_frequencie)
                        st.json(pImportance)


#Text Summarization
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
    nlp = spacy.load("nl_core_news_lg")
    doc = nlp(my_text)
    return doc

def load_lottieurl(url:str):
    """
    This function is used to show an animation on the webpage
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None 

    return r.json()


if __name__ == '__main__':
    main()