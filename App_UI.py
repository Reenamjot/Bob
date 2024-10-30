import streamlit as st
from openai import OpenAI
client = OpenAI(api_key='my-api-key')

def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
    model=model,
    messages=[
    {"role": "system", "content": "You are Bob. Show a report of your teen driving performance" }, 
    {"role": "user", "content": prompt}, ]
)
    return completion.choices[0].message.content

prompt = input("Enter a prompt: ")
response = get_completion(prompt)
print(response)
