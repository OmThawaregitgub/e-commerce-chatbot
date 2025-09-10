# main.py
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
from faq import ingest_faq_data, faq_chain, get_chroma_client, get_faqs_collection, get_embedding_function
from sql import sql_chain
from pathlib import Path

# The semantic router code will be modified to accept the client and encoder
from router import get_semantic_router, router_routes

# Create a shared ChromaDB client and an embedding function
@st.cache_resource
def get_shared_resources():
    chroma_client = get_chroma_client()
    embedding_function = get_embedding_function()
    return chroma_client, embedding_function

chroma_client, encoder = get_shared_resources()

# Ingest FAQ data into the collection
@st.cache_resource
def load_faq_data():
    faqs_path = Path(__file__).parent / "resources/faq_data.csv"
    ingest_faq_data(chroma_client, encoder, faqs_path)

load_faq_data()

# Create the router using the shared resources
router = get_semantic_router(
    routes=router_routes,
    encoder=encoder,
    index_name='faqs',
    chroma_client=chroma_client
)


def ask(query):
    route = router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    else:
        return f"Route {route} not implemented yet"

st.title("E-commerce Bot")

query = st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user", "content":query})

    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
