import os

import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
import pandas
from dotenv import load_dotenv

load_dotenv()


ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name='sentence-transformers/all-MiniLM-L6-v2'
        )

chroma_client = chromadb.Client()
groq_client = Groq()
collection_name_faq = 'faqs'

def get_chroma_client():
    return chromadb.Client()


# Take path of csv file and inject that in vector database.
def ingest_faq_data(path):
    # It check the collection exist or not, if not then create a new collection and ingest the data.
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print("Ingesting FAQ data into Chromadb...")
        # Create a new collection
        collection = chroma_client.create_collection(
            name=collection_name_faq,
            embedding_function=ef
        )
        df = pandas.read_csv(path)
        docs = df['question'].to_list()
        # We have to add metadata in the form of dictionary.
        metadata = [{'answer': ans} for ans in df['answer'].to_list()]
        # Generate unique IDs for each document
        ids = [f"id_{i}" for i in range(len(docs))]
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
        print(f"FAQ Data successfully ingested into Chroma collection: {collection_name_faq}")
    else:
        print(f"Collection: {collection_name_faq} already exist")

# It will return the revalvant Q&A pairs from the vector database.
def get_relevant_qa(query):
    collection = chroma_client.get_collection(
        name=collection_name_faq,
        embedding_function=ef
    )
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result

# Calling LLM to generate the answer based on the context.
def generate_answer(query, context):
    prompt = f'''Given the following context and question, generate answer based on this context only.
    If the answer is not found in the context, kindly state "I don't know". Don't try to make up an answer.
    
    CONTEXT: {context}
    
    QUESTION: {query}
    '''
    # Call the Groq LLM to generate the answer.
    completion = groq_client.chat.completions.create(
        model=os.environ['GROQ_MODEL'],
        messages=[
            {
                'role': 'user', # Root user
                'content': prompt # The content of the message
            }
        ]
    )
    return completion.choices[0].message.content

# It generate the answer for the given query.
def faq_chain(query):
    result = get_relevant_qa(query)
    # Combine all the answers from the metadata of the results to form a context.
    context = "".join([r.get('answer') for r in result['metadatas'][0]])
    print("Context:", context)
    # Call the generate_answer function to get the final answer.
    answer = generate_answer(query, context)
    return answer


if __name__ == '__main__':
    ingest_faq_data(faqs_path)
    query = "what's your policy on defective products?"
    query = "Do you take cash as a payment option?"
    # result = get_relevant_qa(query)
    answer = faq_chain(query)
    print("Answer:",answer)
