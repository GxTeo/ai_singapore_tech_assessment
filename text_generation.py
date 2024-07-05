import os
import requests

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
    
	return response.json()

if __name__ == "__main__":

    prompt = input("Enter your input: ")
    
    output = query({
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 50,
            "num_return_sequences": 1,
            "temperature": 0.8
        }
    })

    generated_text = output[0]['generated_text']

    print('Input:', prompt)
    print('Generated Text:', generated_text)
