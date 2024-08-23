import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

openai_key = os.getenv("OPENAI_APIKEY")
st.title("Keyword Extractor")

def extract_keywords(paragraph):
    prompt = f"Extract the most important keywords from the following paragraph, the keywords must represent information about the guest stay at the hotel, the information must have relevance, reformulate if needed: {paragraph}"
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    answers = llm.invoke(prompt)
    return answers.content

with st.form("keyword_extractor_form"):
    paragraph = st.text_area("Enter a Paragraph")

    submitted = st.form_submit_button("Extract Keywords")
    if submitted and paragraph:
        keywords = extract_keywords(paragraph)
        st.write("Extracted Keywords:")
        st.write(keywords)
    elif submitted and not paragraph:
        st.error("Please provide a paragraph to proceed.")
