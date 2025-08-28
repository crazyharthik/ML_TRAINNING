from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser # for proper output parsing
from langchain_community.llms import Ollama # Ollama LLM wrapper
import streamlit as st

st.title("Ollama with LangChain")

input_text = st.text_input("Enter your prompt")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Your name is Saravanan Assistant"),
        ("user", f"user query:{input_text}")
    ]
)
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"query": input_text})
    st.write(response)

