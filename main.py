import os
from dotenv import load_dotenv
import streamlit as st
import vertexai
from langchain.llms import Cohere

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# PROJECT_ID = os.getenv("PROJECT_ID")

# vertexai.init(project=PROJECT_ID, location="us-central1")

st.sidebar.title("Virtual Agent (Chatbot) using Open Artificial Intelligence")
st.sidebar.write("This is the graduation project of students from University of Kufa, Department of Electronics and Communications Engineering. It is supervised by Lec. Ammar Mousa. It has been built with a Python backend of LangChain libary with integration from Google Cloud's Vertex AI as the LLM used. The frontend was made possible and hosted by the Python library Streamlit.")
temp = st.sidebar.slider("Temperature", min_value=0, max_value=1, help="Changes the behaviour of the results. \n\n0 ➡️ **Professional** \n\n 1 ➡️ **Creative**")
st.sidebar.link_button("Contact", url="https://t.me/muthanii")


def generate_response(input_text):
    llm = Cohere(
        cohere_api_key=COHERE_API_KEY
    )
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
