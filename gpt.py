from openai import OpenAI

client = OpenAI()

client.api_key = "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"


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
    