import requests
import voice
API_URL = "" #Твой api 
def query(payload):
    response = requests.post(API_URL, json=payload)
    json_data = response.json()
    text_result = json_data.get("text", "")
    return text_result
    
def ask_gpt(prompt:str):
    try:
        output = query({
        "question": prompt
        })
        voice.speaker(output)
    except:
        pass

    

