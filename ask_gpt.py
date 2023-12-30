import requests
import voice
import config


def query(payload):
    response = requests.post(config.API_URL, json=payload)
    json_data = response.json()
    text_result = json_data.get("text", "")
    return text_result


def ask_gpt(prompt: str):
    try:
        output = query({
            "question": prompt
        })
        voice.speaker(output)
    except Exception as e:
        print(f"error: {e}")
