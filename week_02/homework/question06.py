from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

prompt = "What's the formula for energy?"

response = client.chat.completions.create(
    model='gemma:2b',
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0
)

#print(f"Prompt: {prompt} \n Answer: {response.choices[0].message.content}")

import tiktoken

completion_text = response.choices[0].message.content
tokenizer = tiktoken.get_encoding("cl100k_base")  
# https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken

completion_tokens = tokenizer.encode(completion_text)

print(f"Completion Tokens = {len(completion_tokens)}")