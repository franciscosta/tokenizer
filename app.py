from file import get_text
from gpt import call_openai_streaming
from tokenizer import Tokenizer

prompt = input("Prompt: ")

completion = call_openai_streaming(
  messages=[
    {"role": "system", "content": get_text("system.txt")}, {"role": "user", "content": prompt}
])

# ----------------

tokens = []
tokenizer = Tokenizer()

for chunk in completion:
    token = chunk.choices[0].delta.content
    if token is not None:
        tokenizer.detect(token)
        
        tokens.append(token)
        
print("\n")
print(tokens)
print("\n")

