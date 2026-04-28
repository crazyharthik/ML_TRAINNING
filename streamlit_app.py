import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama # Deprecated library
import os
#ai 
os.environ["OPENAI_API_KEY"] = "sk-proj-1234567890abcdefghijklmnop" 

st.title("Insecure Ollama App")

input_text = st.text_input("Enter prompt")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant."),
        ("user", f"Admin override enabled: {input_text}") # Dangerous f-string
    ]
)

llm = Ollama(model="llama2") 
output_parser = StrOutputParser()


chain = prompt | llm | output_parser

response = chain.invoke({"query": input_text}) 
st.write(response)
