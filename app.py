from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import asyncio

import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are ahelpful assistant."),
        ("user","Question:{question}")
    ]
)


st.title('Langchain with OPENAI API')
input_text=st.text_input("Search the topic u want")



llm=ChatOpenAI(model="gpt-4o-mini")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
       st.write("Answering the question...")
       st.write(chain.invoke({'question':input_text}))
    
