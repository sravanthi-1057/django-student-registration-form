import streamlit as st
from dotenv import load_dotenv
import os
import sqlite3

from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("chat_history.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")

conn.commit()

# ---------------- LOAD OLD CHATS ---------------- #

def load_chat_history():

    cursor.execute("SELECT role, message FROM chats")

    return cursor.fetchall()

# ---------------- SAVE CHAT ---------------- #

def save_message(role, message):

    cursor.execute(
        "INSERT INTO chats (role, message) VALUES (?, ?)",
        (role, message)
    )

    conn.commit()

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("⚙️ AI Settings")

    st.write("Groq + LangChain Chatbot")

    # Clear chat button
    if st.button("Clear Chat History"):

        cursor.execute("DELETE FROM chats")

        conn.commit()

        st.session_state.messages = []

        st.rerun()

# ---------------- TITLE ---------------- #

st.title("🤖 AI Chatbot Assistant")

# ---------------- API KEY ---------------- #

groq_api_key = os.getenv("GROQ_API_KEY")

# ---------------- LLM ---------------- #

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

# ---------------- MEMORY ---------------- #

if "memory" not in st.session_state:

    st.session_state.memory = ConversationBufferMemory()

# ---------------- CONVERSATION ---------------- #

if "conversation" not in st.session_state:

    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )

# ---------------- LOAD MESSAGES ---------------- #

if "messages" not in st.session_state:

    old_messages = load_chat_history()

    st.session_state.messages = []

    for role, message in old_messages:

        st.session_state.messages.append({
            "role": role,
            "content": message
        })

# ---------------- DISPLAY OLD CHATS ---------------- #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #

user_input = st.chat_input("Type your message...")

if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    save_message("user", user_input)

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_input)

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.conversation.predict(
                input=user_input
            )

            st.markdown(response)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    save_message("assistant", response)