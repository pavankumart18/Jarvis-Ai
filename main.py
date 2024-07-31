import speech_recognition as sr
import os
import webbrowser
import datetime
import random

import google.generativeai as genai

def chat(query):
    genai.configure(api_key="YOUR_API_KEY")
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
        ]
    )
    # todo: wrap inside of a try catch block
    response = chat_session.send_message(query)
    print(type(response.text))
    say(response.text)




def ai(prompt):
    text=f"gemini response for prompt :{prompt} \n ***************************\n"
    genai.configure(api_key="AIzaSyD5xpKqlMyPxPYYJCeaLKW4v3P88qZEQx0")
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
        ]
    )
    # todo: wrap inside of a try catch block
    response = chat_session.send_message(prompt)
    text+=response.text
    if not os.path.exists("gemini"):
        os.mkdir("gemini")

    with open(f"gemini/prompt- {random.randint(1,23434356)}","w") as f:
        f.write(text)



def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return "Could not request results; check your network connection."

if __name__ == '__main__':
    print("Pycharm")
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening")
        query = takeCommand()
        # todo: Add more sites
        sites=[["Youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],
               ["google","https://google.com"]]
        stop="False"
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} devil...")
                webbrowser.open(site[1])
            if "Thank You".lower() in query.lower():
                stop=True
                break
        # todo: Add a feature to play a specific song
        if "open Music".lower() == query.lower():
            musicPath="/Users/pavankumar/Downloads/basics.mp3"
            os.system(f"open {musicPath}")
        elif "the time".lower() == query.lower():
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"devil the  time is {strfTime}")
        elif "open Facetime".lower() in query.lower():
            os.system("open /System/Applications/FaceTime.app")
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif"Thank You".lower() in query.lower():
            break
        else:
            chat(query=query)

        if stop==True:
            say("Em parledu leyy devil")
            break




