import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

load_dotenv()

# loading the cohere API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm =OpenAI(
        openai_api_key=OPENAI_API_KEY
    )

# working on the sidebar
st.sidebar.title("Virtual Agent (Chatbot) using Open Artificial Intelligence")
st.sidebar.write("This is the graduation project of students from University of Kufa, Department of Electronics and Communications Engineering. It is supervised by Lec. Ammar Mousa. It has been built with a Python backend of LangChain libary with integration from Cohere as the LLM used. The frontend was made possible and hosted by the Python library Streamlit.")
if st.sidebar.toggle("QR Code"):
    st.sidebar.image("./img/QR.png")
st.sidebar.link_button("Contact", url="https://t.me/muthanii", use_container_width=True)
st.sidebar.link_button("GitHub", url="https://github.com/muthanii/grad-proj", use_container_width=True)
container = st.container()
with container:
    st.title("Virtual Agent (Chatbot)", anchor=False)

# function to generate the response
def generate_response(input_text):
    return llm(input_text)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask away!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Bot: {generate_response(prompt)}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
