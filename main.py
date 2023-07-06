import streamlit as st
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import time 



if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def onclick():
    st.session_state.clicked = True

st.title("Article Summarizer")
url = st.text_input('Enter the article link here')
article = Article(url)

# col1, col2 , col3 = st.columns([1,3,1])

st.button('Summarize',on_click=onclick) 


if st.session_state.clicked:
    progressbar = st.progress(0)

    for perc in range(100):
        time.sleep(0.01)
        progressbar.progress(perc+1)

    # st.divider()    
    # st.header('Summary of the article is :')
    article.download()
    article.parse()
    article.nlp()
    st.title(article.title)
    st.divider()
    
    st.caption(article.summary)



    







