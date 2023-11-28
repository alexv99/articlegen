import streamlit
import langchain

streamlit.title('Quickstart App')


def generate_response(input_text):

    # Initialize LangChain
    chat = langchain.LLM(
        model_id="gpt-4",
    )

    # Prompt GPT-4
    prompt = "Write a poem about the beauty of nature."
    response = chat.call(prompt)

    streamlit.info(response)


with streamlit.form('my_form'):
    text = streamlit.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = streamlit.form_submit_button('Submit')
    if submitted:
        generate_response(text)
