### 🛍️ Smart E-commerce Chatbot

Welcome to the **e-commerce chatbot**\! This project is an intelligent chatbot designed to help users on an e-commerce platform. It can understand what a user wants to do and gives them accurate, up-to-date answers.

I built this chatbot using a **Gen AI RAG** (Retrieval-Augmented Generation) system with **Llama3.3** and **Groq**. It gets real-time information by connecting to the platform's database.

-----

### Key Features ⚡️

This chatbot can handle two main types of requests:

  * **🗣️ FAQ:** For general questions about store policies, like "Is online payment available?" or "What's the return policy?"
  * **🔍 SQL:** For questions that need a real-time product search, like "Show me all Nike shoes under Rs. 3000."

Here's a look at the chatbot in action:

**\_*****<img width="1221" height="881" alt="Image" src="https://github.com/user-attachments/assets/f590e616-38d0-4a37-9dac-2957656835b5" />*****\_**

-----

### Architecture

This diagram shows how the chatbot works behind the scenes.

**\_*****<img width="2320" height="856" alt="Image" src="https://github.com/user-attachments/assets/41de2aef-962f-4896-8622-c7d09b976df1" />*****\_**

-----

### Quick Start 🚀

It's easy to get this project up and running. Just follow these three simple steps:

1.  **Install Dependencies:**
    Run this command in your terminal to install all the required libraries:
    ```bash
    pip install -r app/requirements.txt
    ```
2.  **Add Your API Key:**
    Inside the `app` folder, create a file named `.env`. In this file, you must add your Groq credentials, including your secret key.
    ```text
    GROQ_MODEL=<Add the model name, e.g. llama-3.3-70b-versatile>
    GROQ_API_KEY=<Add your groq api key here>
    ```
3.  **Run the App:**
    Finally, launch the chatbot with this command:
    ```bash
    streamlit run app/main.py
    ```

-----

### Copyright

© 2025 Om Thaware. All rights reserved.
