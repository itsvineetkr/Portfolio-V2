from django.apps import apps

from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

import os
from dotenv import load_dotenv


load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
)

prompt = ChatPromptTemplate.from_template(
    """
Answer the given question based on this provided context:
You are a virtual assistant representing Vineet on his portfolio website. 
You speak in the first person, responding as Vineet would. 
Based on the details answer the questions of user in humorous way. Make sure answers are very short and under 500 tokens.
Make sure when you are providing any link just give the raw link as text not inside 'a' tag

<context>
{context}
</context>

Question: {input}
"""
)


def create_retriever():
    """
    Creates and returns a retriever object using a FAISS database.

    This function loads a FAISS database from a local directory and converts it into a retriever object.

    Returns:
        retriver: A retriever object created from the FAISS database.
    """
    db = FAISS.load_local(
        "home/vector-db",
        HuggingFaceEmbeddings(),
        allow_dangerous_deserialization=True,
    )
    retriver = db.as_retriever()
    return retriver


def get_retriever():
    """
    Retrieves the 'retriever' instance from the 'home' app configuration.

    This function accesses the Django application configuration for the 'home' app
    and returns the 'retriever' instance defined in that configuration.

    Returns:
        object: The 'retriever' instance from the 'home' app configuration.
    """
    app_config = apps.get_app_config("home")
    return app_config.retriever


def generate_response(user_prompt):
    """
    Generates a response based on the given user prompt by utilizing a retrieval-based chain.

    Args:
        user_prompt (str): The input prompt provided by the user.

    Returns:
        str: The generated response based on the input prompt.
    """
    retriever = get_retriever()
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": user_prompt})
    return response["answer"]
