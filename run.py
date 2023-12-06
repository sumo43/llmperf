import time
import requests

st = time.time()
url = "http://localhost:8000/v2/models/ensemble/generate"
prompt = "hello my name is "
payload = {
        "text_input": "hello my name is ",
        "bad_words": "",
        "stop_words": "",
        "max_tokens": 32,
        "end_id": 2
}

headers = {
        "accept": "application/json",
        "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
response.raise_for_status()
words = response.json()["text_output"]
print("prompt")
print(prompt)
print("words")
print(words)
exit(0)
et = time.time()
