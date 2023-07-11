import streamlit as st

import nltk
from textblob import TextBlob
from newspaper import Article
import time 

nltk.download('punkt')

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def onclick():
    st.session_state.clicked = True

def computeanddisplay():
    article.download()
    article.parse()
    article.nlp()
    st.header(article.title)
    st.divider()
    st.header("Summary:")
    st.write(article.summary)

    st.divider()
    st.header("sentiment:")
    analysis = TextBlob(article.text)
    if analysis.polarity>0:
        st.write("Sentiment of the article is positive")
    else:
        st.write("Sentiment of the article is negative")  



    
st.set_page_config(page_title="Article-Summarizer", page_icon="📝")

st.markdown("""
    <style type="text/css">
    [data-testid=stSidebar] {
        background-color: rgb(70, 100, 200);
        color: #FFFFFF;
    }
    
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Instructions to use the page")

st.sidebar.markdown("""
    * Copy paste the link of the Article
    * Press the button summarize 
    * Wait for the results 
    * Checkout  the title, summary and sentiment analysis of the article
    """)

with st.sidebar.expander("Tech used"):
    st.markdown("""
 * Streamlit 
 * NLTK - NLP
 * Textblob
 * Newspaper3k""")    

with st.sidebar.expander("Credits"):
    st.markdown("""
 * Adithya R 
 * Karan P
 * Aditya Verma
 * Deepa G""")


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

    st.title("Title:")
    st.divider()
    computeanddisplay()



    







