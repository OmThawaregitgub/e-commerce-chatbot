from semantic_router import Route, RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

"""
The function is use for routing purpose
means user queri is related to which topic.In that we have to define the topics.
For example FAQ,SQL etc. and then we have to define the utterances for each topic.
"""
encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    # If this utterance is present in the user query then it will route to faq topic.
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
    ]
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ]
)

router = RouteLayer(routes=[faq, sql], encoder=encoder)

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)