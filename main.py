import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import Cohere
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from langchain.agents import initialize_agent

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

llm = Cohere(
        cohere_api_key=COHERE_API_KEY
    )

search = WikipediaAPIWrapper()

tool = Tool(
    name='Wikipedia',
    func=search.run(),
    description='Useful for searching for recent data.'
)

agent = initialize_agent(
    agent='zero-shot-react-description',
    tools=tool,
    llm=llm,
    verbose=True,
    max_iterations=3
)

st.sidebar.title("Virtual Agent (Chatbot) using Open Artificial Intelligence")
st.sidebar.write("This is the graduation project of students from University of Kufa, Department of Electronics and Communications Engineering. It is supervised by Lec. Ammar Mousa. It has been built with a Python backend of LangChain libary with integration from Cohere as the LLM used. The frontend was made possible and hosted by the Python library Streamlit.")
if st.sidebar.toggle("QR Code"):
    st.sidebar.image("./img/QR.png")
st.sidebar.link_button("Contact", url="https://t.me/muthanii", use_container_width=True)
st.sidebar.link_button("GitHub", url="https://github.com/muthanii/grad-proj", use_container_width=True)
container = st.container()
with container:
    st.title("Virtual Agent (Chatbot)", anchor=False)


def generate_response(input_text):
    return agent.run(input_text)


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
