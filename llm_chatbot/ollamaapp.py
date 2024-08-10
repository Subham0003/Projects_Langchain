import streamlit    as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Ollama"

#creating chatprompt

prompt=ChatPromptTemplate([
    ('system',"you are a helpful assistand and your job is to assit to the user accroding to their query"),
    ('user','Question:{question}'),
])


def response_generator(question,llm,temperature,max_tokens):
    
    llm=Ollama(model=llm)
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer=chain.invoke({'question':question})
    return answer


## #Title of the app
st.title("Enhanced Q&A Chatbot With OLLAMA")


## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["llama2:latest"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    response=response_generator(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")