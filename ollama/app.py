import os
from dotenv import load_dotenv
load_dotenv()


from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


##creating template

template = ChatPromptTemplate.from_messages([
    ("You are an AI assistant. You will be given a task. You must generate a detailed and long answer. While answering think step-by-step and justify your answer"),
    ("user","Question:{question}")

])

##creating LLM

llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain=template|llm|output_parser

#creating streamlit framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")

if input_text:
    st.write(chain.invoke({'question':input_text}))