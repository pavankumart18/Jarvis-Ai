import os

# Print the API key to verify it is correctly set (for debugging purposes only, remove in production)
from config import apikey

import openai

# Read the API key from an environment variable
openai.api_key = apikey

if openai.api_key is None:
    raise ValueError("API key is missing. Please set the OPENAI_API_KEY environment variable.")

# Using the correct method for the appropriate model
response = openai.completions.create(
    model="gpt-3.5-turbo",
    prompt="Hello, how can I use the OpenAI API to generate completions?",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response
print(response.choices[0].text.strip())
