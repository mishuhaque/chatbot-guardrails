import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8000/improve"
    payload = {
        "query": "When was DeepSeek released?",
        "response": "DeepSeek was released in 2022."
    }
    res = requests.post(url, json=payload)
    print(res.json())
