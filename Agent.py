from config import key
from speech import mic1
import task1
import requests #web
from text import text_to_speech_and_play


def parse_function_response(message):
    function_call=message[0].get("functionCall")
    function_name=function_call["name"]
    print("Gemini: call function ",function_name)
    try:
        arguments=function_call.get("args","Barnala")
        print("Gemini arguments are ",arguments)
        if arguments:
            d=getattr(task1,function_name)
            print("function is ",d)
            function_response=d(**arguments)
        else:
            function_response="No Arguments are present"


    except Exception as e:
        print(e)
        function_response="Invalid function"
    return function_response

def run_conversation(user_message):
    messages=[] 
    system_message ="You are an AI bot named Jarvis and created by gorav jindal and his team who also played a very vital role in creating you as well.As a Ai bot you can do everything using function call. when you are asked to do something, use the function call you have available and then respond with message"

    message={"role": "user", "parts": [{"text": system_message + "\n"+user_message }] }
    
    messages.append(message)

    data={"contents": [messages],
          "tools": [
              {
                  "functionDeclarations":task1.definitions
              }
          ]
        }

    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data)
    if (response.status_code !=200):
        print(response.text)

    t1=response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No Content in Response") 

    
    message=t1.get("candidates")[0].get("content").get("parts")
    if 'functionCall' in message[0]:
        resp1=parse_function_response(message)
        return resp1
    else:
        return("Sorry but i can't assist you")




if (__name__)=="__main__":
    user_message="find the ip address of google.com"
    print(run_conversation(user_message))