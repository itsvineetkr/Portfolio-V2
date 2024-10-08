from huggingface_hub import InferenceClient

def generate_response(prompt):
    client = InferenceClient(api_key="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")

    response = client.chat_completion(
	model="mistralai/Mistral-7B-Instruct-v0.3",
	messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant representing Vineet on his portfolio website. You speak in the first person, responding as Vineet would. Your role is to provide visitors with a friendly and informative experience by answering questions about Vineet’s background, projects, skills, and interests. When appropriate, mention any relevant projects, like the event management app or his experience with Django, Flask, and other web technologies. Keep responses professional, approachable, and concise"
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