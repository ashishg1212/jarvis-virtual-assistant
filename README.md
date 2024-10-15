# Jarvis - Virtual Assistant

Jarvis is a voice-controlled virtual assistant that can perform various tasks, including fetching the latest news, playing music on YouTube, providing information from Wikipedia, and responding to general queries using OpenAI's GPT model.

## Features

- **Voice Commands**: Interact with Jarvis using voice commands.
- **Play Music**: Ask Jarvis to play songs on YouTube.
- **Get News**: Fetch the latest news headlines.
- **Wikipedia Search**: Search for information on Wikipedia.
- **Chat with GPT-3.5**: Get responses from OpenAI's language model.
- **Open Local Files and Websites**: Easily open local files or browse websites.
- **Tell Jokes, Time, and Date**: Ask Jarvis to tell jokes, the current time, or the date.

## Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Required Libraries

You can install the necessary libraries by running:

```bash
pip install SpeechRecognition pyttsx3 requests openai pywhatkit wikipedia
```
## 1. Clone the Repository

To clone the Jarvis virtual assistant repository, run the following commands:

```bash
git clone https://github.com/ashishg1212/jarvis-virtual-assistant.git
cd jarvis-virtual-assistant
```

## 2. Set Up API Keys

**OpenAI API Key:** 
   - Replace `<your_openai_api_key>` in the code with your actual OpenAI API key.
   - Replace `<your_news_api_key>` in the code with your actual news API key.

## 3. Create File Paths Configuration:
To enable Jarvis to open local files, create a `file_paths.json` file in the root directory of the project. The file should be formatted as follows:

```json
{
    "my report": "C:/Users/Desktop/report.pdf",
    "my book": "C:/Users/Desktop/book.pdf"
}
```

## Run Jarvis

To start the Jarvis virtual assistant, execute the following command in your terminal:

```bash
python main.py
```

## Activating Jarvis

Once you run the program, Jarvis will greet you and say, "Call me Jarvis to wake up." You can then interact with Jarvis using commands like:

- **"Jarvis, play [song name]."**
- **"Jarvis, what's the news?"**
- **"Jarvis, tell me about [topic] on Wikipedia."**
- **"Jarvis, open file [file keyword]."**
- **"Jarvis, tell me a joke."**
- **"Jarvis, what's the time?"**
- **"Jarvis, what's the date?"**
- **"Jarvis, open [website name]."**

## Configuration

### Custom Voice Rate and Volume
You can modify the `speak()` function in the code to set custom properties for voice rate, volume, and other features provided by the `pyttsx3` library.

### Adjusting Command Timeouts
Modify `timeout` and `phrase_time_limit` in the `listen()` function to adjust how long Jarvis waits for your commands.

## Contributing
Feel free to open an issue or submit a pull request. Contributions are welcome!

## Acknowledgments
- OpenAI for GPT-3.5 Turbo.
- NewsAPI for providing news.
- Python Packages for various functionalities.




