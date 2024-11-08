from huggingface_hub import InferenceClient
from .constants import init_prompt
from dotenv import load_dotenv
import os

load_dotenv()

def generate_response(prompt):
    client = InferenceClient(api_key="")

    response = client.chat_completion(
	model="mistralai/Mistral-7B-Instruct-v0.3",
	messages=[
            {
                "role": "system",
                "content": init_prompt
            },
            {
                "role": "user",
                "content": prompt,
            },
    ],
	max_tokens=500,
	stream=False,
    )

    return response["choices"][0]["message"]["content"]