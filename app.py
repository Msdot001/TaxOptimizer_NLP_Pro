import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import spacy


def text_analizer(my_text):
    nlp = spacy.load("nl_core_news_lg")
    doc = nlp(my_text)

    data = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_)) for token in doc]
    return data

#Change default name of app on Browser Tab
st.set_page_config(page_title='TextOptimizer App', layout="wide")
st.title("Text Optimizer NLP App")
st.subheader("Choose your NLP Solution and Enter your Text:")

def main():
    """
    This main function is called to execute the code to run the app
    """
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
            nlp_result = text_analizer(message)
            st.json(nlp_result)
    #Named Entity

    #Text Summarization



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