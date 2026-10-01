# 🤖 JARVIS – Python Voice Assistant

JARVIS is a Python-based voice assistant that allows users to interact with a computer using voice commands.

The application listens to the user's voice through the microphone, converts speech into text, identifies the requested command, performs the corresponding action, and responds using text-to-speech.

---

## 🚀 Features

* 🎤 Voice input using microphone
* 🗣️ Speech-to-text conversion
* 🔊 Text-to-speech response
* ⏰ Current time detection
* 🤖 JARVIS name response
* 🌐 Open Google using voice
* 💻 Open LeetCode using voice
* 📚 Search Wikipedia using voice
* 📝 Application logging
* ⚠️ Error handling for microphone and speech-recognition failures
* 👋 Time-based greeting
* 🛑 Voice-controlled exit

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       USER          │
                         │   Speaks Command    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Microphone      │
                         │    Audio Input      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │    Speech Recognition       │
                    │       SpeechRecognition     │
                    │                              │
                    │       Speech → Text         │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │   Command Handler   │
                         │   handle_command()  │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
      │ Time Command │      │ Web Commands  │      │  Wikipedia   │
      │              │      │              │      │    Search    │
      └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
             │                     │                     │
             └─────────────────────┼─────────────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │    Response Text    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      pyttsx3        │
                         │    Text → Speech    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Speaker        │
                         │     🔊 Voice        │
                         └─────────────────────┘


             ┌─────────────────────────────┐
             │       Logging System       │
             │                             │
             │ logs/application.log        │
             └─────────────────────────────┘
```

---

# 🔄 Application Workflow

```text
START
  │
  ▼
Initialize Logging
  │
  ▼
Initialize Text-to-Speech
  │
  ▼
JARVIS Greets User
  │
  ▼
Listen Through Microphone
  │
  ▼
Convert Speech → Text
  │
  ▼
Normalize Command
  │
  ▼
Identify Command
  │
  ├── "time"
  │      └── Get current time → Speak result
  │
  ├── "name"
  │      └── Tell assistant name
  │
  ├── "open google"
  │      └── Open Google → Speak response
  │
  ├── "open leetcode"
  │      └── Open LeetCode → Speak response
  │
  ├── "wikipedia"
  │      └── Search Wikipedia → Speak summary
  │
  ├── "exit" / "quit"
  │      └── Goodbye → STOP
  │
  └── Unknown / Empty
         └── Listen again
```

---

# 🧩 Project Components

## 1. Speech Recognition

The microphone captures the user's voice.

```python
audio = r.listen(
    source,
    timeout=5,
    phrase_time_limit=10
)
```

The captured audio is converted into text using:

```python
query = r.recognize_google(
    audio,
    language="en-in"
)
```

The project uses Indian English recognition with `en-in`.

---

## 2. Text-to-Speech

JARVIS uses `pyttsx3` with the Windows SAPI5 speech engine.

```python
engine = pyttsx3.init("sapi5")
```

The `speak()` function converts response text into audio.

```python
def speak(text):
    engine.say(text)
    engine.runAndWait()
```

---

## 3. Command Processing

The main command-processing logic is inside:

```python
handle_command(query)
```

The query is first normalized:

```python
query = query.lower().strip()
```

Then the application checks for supported commands.

Example:

```python
if "time" in query:
    ...
elif "name" in query:
    ...
elif "open google" in query:
    ...
```

---

# 🎯 Supported Commands

| Voice Command        | Action                        |
| -------------------- | ----------------------------- |
| `What is the time?`  | Speaks current time           |
| `What is your name?` | Says JARVIS                   |
| `Open Google`        | Opens Google                  |
| `Open LeetCode`      | Opens LeetCode contest page   |
| `Wikipedia Python`   | Searches Wikipedia for Python |
| `Exit`               | Stops JARVIS                  |
| `Quit`               | Stops JARVIS                  |

---

# 📚 Wikipedia Search

JARVIS can search Wikipedia through voice.

Example:

```text
User:
"Wikipedia artificial intelligence"

        ↓

Remove "wikipedia"

        ↓

"artificial intelligence"

        ↓

Wikipedia

        ↓

2 sentence summary

        ↓

JARVIS speaks result
```

The implementation uses:

```python
result = wikipedia.summary(
    topic,
    sentences=2
)
```

It also handles cases such as ambiguous Wikipedia results and missing pages.

---

# 📝 Logging

The application creates a `logs` directory automatically.

```text
project/
│
├── main.py
├── requirements.txt
│
└── logs/
    └── application.log
```

Logging is configured using:

```python
logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s ] - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
```

User commands and application errors can therefore be recorded in the log file.

---

# 📁 Project Structure

```text
JARVIS/
│
├── main.py
│
├── requirements.txt
│
└── logs/
    └── application.log
```

### `main.py`

Contains the complete JARVIS application:

* Logging setup
* Text-to-speech
* Speech recognition
* Greeting
* Command handling
* Browser operations
* Wikipedia search
* Main application loop

### `requirements.txt`

Contains the Python dependencies:

```text
SpeechRecognition==3.10.0
pyttsx3
pyaudio
wikipedia
```

---

# ⚙️ Installation

## Step 1 — Clone the Repository

```bash
git clone <your-repository-url>
```

Go inside the project:

```bash
cd JARVIS
```

---

## Step 2 — Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

You should see:

```text
(venv)
```

in your terminal.

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

The project requires:

```text
SpeechRecognition
pyttsx3
PyAudio
wikipedia
```

---

# Step 4 — Run the Application

```bash
python main.py
```

You should see something similar to:

```text
Listening...
```

Speak a command.

For example:

```text
Open Google
```

JARVIS will process the command and open Google.

---

# 🎤 How to Use

After starting the application:

```text
python main.py
```

JARVIS greets the user according to the current time.

```text
Good Morning!
```

or

```text
Good Afternoon!
```

or

```text
Good Evening!
```

Then:

```text
I am JARVIS!! How can I help you today?
```

The application continuously listens for commands until the user says:

```text
Exit
```

or:

```text
Quit
```

The main loop continuously calls the microphone and command handler.

---

# 🧪 Example Session

```text
JARVIS:
Good Evening!

JARVIS:
I am JARVIS!! How can I help you today?

User:
What is the time?

JARVIS:
The time is 19:30:25

User:
Open Google

JARVIS:
Opening Google.

User:
Open LeetCode

JARVIS:
Sir I have opened LeetCode for you.

User:
Wikipedia machine learning

JARVIS:
According to Wikipedia...

[Wikipedia summary]

User:
Exit

JARVIS:
Goodbye! Have a great day!
```

---

# 🛠️ Error Handling

The application handles several runtime problems.

### Microphone timeout

If nothing is heard:

```text
I did not hear anything.
```

### Microphone unavailable

The application reports:

```text
I cannot access the microphone.
```

### Speech not understood

The application says:

```text
Say that again please...
```

### Speech recognition service unavailable

The application reports:

```text
Speech recognition is unavailable.
Check your internet connection.
```

These cases are handled inside `take_command()`.

---

# 🧠 Technology Stack

```text
Programming Language
        │
        ▼
     Python
        │
        ├───────────────┐
        ▼               ▼
Speech Recognition   Text-to-Speech
        │               │
SpeechRecognition    pyttsx3
        │               │
        ▼               ▼
 Google Speech       Windows SAPI5
        │
        └───────────────┐
                        ▼
                  Command Handler
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Browser       Wikipedia       Time
```

### Technologies

* **Python**
* **SpeechRecognition**
* **Google Speech Recognition**
* **pyttsx3**
* **Windows SAPI5**
* **PyAudio**
* **Wikipedia**
* **Python Logging**
* **Webbrowser**

---

# 🔐 Current Architecture Type

This project currently uses a:

**Rule-Based Command Architecture**

The assistant determines the action by checking whether predefined phrases exist in the recognized query.

For example:

```python
if "time" in query:
```

```python
elif "open google" in query:
```

```python
elif "wikipedia" in query:
```



# 🐛 Troubleshooting

## PyAudio Installation Problem

If you receive an error related to `pyaudio` while installing dependencies, make sure you are using a supported Python environment and that the required audio dependencies are installed.

Check:

```bash
python --version
```

Then retry:

```bash
pip install pyaudio
```

---

## Microphone Not Working

Check:

1. Microphone is connected.
2. Windows has microphone permission enabled.
3. Your microphone is selected as the default input device.
4. PyAudio is installed correctly.

---

## Wikipedia Not Working

Wikipedia functionality requires network access.

Check your internet connection and try:

```text
Wikipedia Python
```

---

# 📌 Project Objective

The main objective of this project is to demonstrate how a Python application can combine:

```text
Speech Recognition
        +
Natural Voice Output
        +
Command Processing
        +
Web Automation
        +
Information Retrieval
        +
Application Logging
```

to create a basic desktop voice assistant.

---

# 👨‍💻 Project Flow in One Line

```text
User Voice → Microphone → Speech-to-Text → Command Handler → Action → Text-to-Speech → User
```

---

# 📄 License

This project is created for learning and educational purposes.
