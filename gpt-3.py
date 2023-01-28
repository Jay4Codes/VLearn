import requests

# from transformers import pipeline, set_seed

# summarizer = pipeline('text2text-generation', model='describeai/gemini')
# code = "print('hello world!')"

# response = summarizer(code, max_length=100, num_beams=3)
# print("Summarized code: " + response[0]['generated_text'])

API_URL = "https://api-inference.huggingface.co/models/describeai/gemini"
headers = {"Authorization": f"Bearer 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"}

text = "useEffect(()=> { alanBtn({key: '1cd1c991b78573fc8c9c034eaa1d05ef2e956eca572e1d8b807a3e2338fdd0dc/stage',})}, [])"


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


lines = text.splitlines()
for i in lines:
    output = query({
        "inputs": "def suck_dick(): pass",
    })          

    print(output)
