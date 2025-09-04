💬 E-commerce Chatbot
This project is an intelligent chatbot for an e-commerce website. It's built to understand what a user is asking for and give them the right answer. The bot connects to a database in real time to make sure its information is always correct and up-to-date.

What the Bot Can Do
The chatbot can handle two main types of questions:

FAQs (Frequently Asked Questions): This is for when people ask about the store's policies or general information, like "Do you accept online payments?"

Product Questions: This is for when people want to find products. The bot can search the database in real time for specific items. For example, "Show me all Nike shoes under Rs. 3000."

How to Get Started
1. Set Up the Project
To get the project ready, you need to install all the necessary files. You can do this by running a single command:

Bash

pip install -r app/requirements.txt
2. Add Your Groq Credentials
Inside the app folder, you need to create a new file named .env. In this file, you'll add your personal Groq API key and the name of the model you want to use.

Plaintext

GROQ_MODEL=<Add the model name, e.g. llama-3.3-70b-versatile>
GROQ_API_KEY=<Add your groq api key here>
3. Run the App
After you've completed the steps above, you can start the chatbot by running this command:

Bash

streamlit run app/main.py