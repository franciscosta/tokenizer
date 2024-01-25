import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY_WORK")

if not api_key:
    raise ValueError("No API key found. Set the OPENAI_API_KEY environment variable.")

client = OpenAI()
client.api_key = api_key

def call_openai_streaming(messages, model="ft:gpt-3.5-turbo-1106:superlistcom::8hmlRcI5"):
    return client.chat.completions.create(
            model=model, messages=messages, stream=True)
    
    # for message in response_stream:
    #   if 'content' in message:
    #     yield message['content']


def call_openai(messages, model="ft:gpt-3.5-turbo-1106:superlistcom::8diNGSDG"):
    return ( client.chat.completions.create(
            model=model, messages=messages)
          ).choices[0].message.content
    