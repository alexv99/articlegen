import streamlit
from langchain.llms.openai import OpenAI

streamlit.title('Quickstart App')


def generate_response(input_text):
    # Initialize LangChain
    llm = OpenAI(model_name="gpt-4")
    # Prompt GPT-4
    response = llm.invoke(input_text)
    streamlit.info(response)


with streamlit.form('my_form'):
    text = streamlit.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = streamlit.form_submit_button('Submit')
    if submitted:
        generate_response(text)
