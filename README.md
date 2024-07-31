# Jarvis A.I

Jarvis A.I is a personal assistant that can take voice commands, respond with synthesized speech, and perform various tasks such as opening websites, playing music, telling the time, and interacting with Google's generative AI model, Gemini.

## Features

- **Voice Commands:** Recognize and process voice commands using `speech_recognition`.
- **Text-to-Speech:** Respond to commands with synthesized speech using the system's `say` command.
- **Web Browsing:** Open popular websites like YouTube, Wikipedia, and Google.
- **Play Music:** Play a specific song from the local directory.
- **Tell the Time:** Announce the current time.
- **AI Interaction:** Generate responses using Google's generative AI model, Gemini.

## Requirements

- Python 3.x
- `speech_recognition` library
- `google-generativeai` library
- Microphone for voice input
- Internet connection for online services

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/jarvis-ai.git
   cd jarvis-ai

## Install Dependencies
    pip install speechrecognition google-generativeai

## Set up API KEY

Replace YOUR_API_KEY with your Google API key in the chat and ai functions.

## Usage

1. **Run the Main Script::**
   ```bash
   python main.py

2. **Vocal Commands:**
    Say "Open [site]" to open a website (e.g., "Open YouTube").
    Say "open Music" to play the specified song.
    Say "the time" to hear the current time.
    Say "open Facetime" to open the FaceTime app.
    Say "Using artificial intelligence" followed by a prompt to generate a response using the AI model.
    Say "Thank You" to stop the assistant.

## Example Commands
    Open YouTube

    open Music

    the time

    Using artificial intelligence, tell me a joke.

## LICENSE
    This project is licensed under the MIT License. See the LICENSE file for details.

## ACKNOWLEDGEMENTS
    SpeechRecognition
    Google Generative AI



