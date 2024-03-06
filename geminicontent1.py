from config import key
from speech import mic1
from task1 import temp_city
import requests #web

def chat1(chat):
    messages=[] 
    system_message ="You are an AI bot, your name is Jarvis made by Gorav "

    message={"role": "user", "parts": [{"text": system_message + " "+chat }] }
    messages.append(message)

    data={"contents": messages}

    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data)
    t1= response.json()
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)


chat=mic1()
chat1(chat)

