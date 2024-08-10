import streamlit    as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import openai

## Load OpenAI API Key
## Load OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = api_key




#creating chatprompt

prompt=ChatPromptTemplate([
    ('system',"you are a helpful assistand and your job is to assit to the user accroding to their query"),
    ('user','Question:{question}'),
])

def response_generator(question,api_key,engine,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=engine)
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer=chain.invoke({'question':question})
    return answer


## #Title of the app
st.title("Hy Buddy,I am  fucking awesome AKash.I know everylittle thing .Come to me i will give you all Gyan of the world")

## Sidebar for settings
st.sidebar.title("Settings")



## Select the OpenAI model
engine=st.sidebar.selectbox("Select Open AI model",["gpt-4o","gpt-4-turbo","gpt-4"])

## Temperature for the model
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)

## Maximum tokens for the response
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


## MAin interface for user input
st.write("Try me & you wont regret")
user_input=st.text_input("You:")

if user_input and api_key:
    response=response_generator(user_input,api_key,engine,temperature,max_tokens)
    st.write(response)

elif user_input:
    st.warning("Please enter the OPen AI aPi Key in the sider bar")
else:
    st.write("Please provide the user input")

