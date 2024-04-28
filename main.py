# Press the green button in the gutter to run the script.
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import openai

# openai.api_key = os.getenv('OPENAI_API_KEY', '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')
#
# chatStr = ""
#
# def chat(query):
#     global chatStr
#     print(chatStr)
#     chatStr += f"Harsh: {query}\n Jarvis: "
#     completion = openai.Completion.create(
#         engine="gpt-3.5-turbo-1106",
#         prompt=chatStr,
#         max_tokens=50
#     )
#
#     try:
#         say(completion.choices[0].text.strip())
#         chatStr += f"{completion.choices[0].text.strip()}\n"
#         return completion.choices[0].text.strip()
#     except Exception as e:
#         print("Error:", e)
#         return "Error occurred during conversation"


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis AI')
    say("Hello, I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")
            print(f"Sir time is {hour} bajke {min} minutes")

        elif "jarvis stop".lower() in query.lower():
            exit()

        # else:
        #     print("chatting..")
        #     chat(query)