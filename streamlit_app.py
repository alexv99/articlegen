import streamlit as st
from langchain.llms import OpenAI
from langchain.llms import GPT
from langchain.chains import SingleModelChain

st.title('Quickstart App')
openai_api_key = "st.sidebar.text_input('OpenAI API Key')"

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, model_name="gpt-4")
    # Configuration for GPT-4
    gpt_config = {
        "model_name": "gpt-4",
        "max_tokens": 100
    }
    # Create a GPT object with the configuration
    gpt = GPT(**gpt_config)

    # Instantiate LangChain with the GPT model
    chain = SingleModelChain(gpt)

    # Sending a prompt to GPT-4 and getting a response
    response = chain.run(input_text)  

    st.info(response)

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
