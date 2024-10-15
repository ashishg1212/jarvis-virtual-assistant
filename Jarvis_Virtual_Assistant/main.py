import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import openai
import pywhatkit
import datetime
import wikipedia
import os
import random
import json

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
openai_api_key = "<your_openai_api_key>"  # Replace with your actual OpenAI API key
news_api_key = "<your_news_api_key>"  # Replace with your actual NewsAPI key

def speak(text):
    # engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def ai_process(command):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis. Give short responses please"},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Error: {e}")
        speak("I'm currently unable to process this request. Please try again later.")
        return None

def load_file_paths():
    try:
        with open("file_paths.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file paths: {e}")
        return {}

def process_command(command):
    command = command.lower()

    # Open a local application or file
    if "open file" in command:
        file_mappings = load_file_paths()
        for key in file_mappings:
            if key in command:
                try:
                    os.startfile(file_mappings[key])
                    speak(f"Opening {key}")
                    return
                except Exception as e:
                    speak(f"Unable to open {key}.")
                    print(f"Error: {e}")
                    return
    
    # Open website
    elif "open " in command:
        site = command.replace("open ", "").strip()
        if "." in site:
            webbrowser.open(f"https://{site}")
            speak(f"Opening {site}")
        else:
            speak(f"Opening {command}")
            webbrowser.open(f"https://www.google.com/search?q={site}")

    # Fetch the latest news
    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    speak("Here are the top headlines:")
                    for i, article in enumerate(articles[:5], 1):  
                        speak(f"Headline {i}: {article['title']}")
                else:
                    speak("I couldn't find any news articles.")
            else:
                speak("I'm unable to fetch news at the moment. Please try again later.")
        except Exception as e:
            print(f"Error fetching news: {e}")
            speak("I'm currently unable to fetch the news. Please try again later.")
    
    # Play music on YouTube
    elif "play" in command:
        song = command.replace('play', '').strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    
    # Tell current time
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}")
    
    # Tell current date
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {current_date}")

    # Search Wikipedia
    elif 'wikipedia' in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "").strip()
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    
    # Tell a joke
    elif 'joke' in command:
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts.",
            "I would tell you a construction joke, but I'm still working on it.",
            "Why do cows have hooves instead of feet? Because they lactose."
        ]
        joke = random.choice(jokes)
        speak(joke)
    
    # Other commands using OpenAI
    else:
        response = ai_process(command)
        if response:
            speak(response)

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Call me Jarvis to wake up")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not catch that. Could you say it again?")
            return None
        except sr.RequestError:
            print("Network error. Please check your internet connection.")
            return None

if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        if command and "jarvis" in command:
            speak("Yes, tell me.")
            command = listen()
            if command:
                process_command(command)
