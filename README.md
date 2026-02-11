#🎙️ Text & Speech Convertor  
Multi-Feature Voice Assistant Desktop Application  

Text & Speech Convertor is a Python-based desktop application built using Tkinter that enables users to convert text to speech, speech to text, and audio files to text. It also provides word cloud visualization and real-time word count for enhanced text analysis and interaction.

This project focuses on building an interactive GUI application integrated with speech processing and audio handling capabilities.

---

🚀 Key Features  

🔹 Text-to-Speech Conversion  
- Convert typed text into natural-sounding speech  
- Supports male and female voice options  
- Adjustable playback speed  

🔹 Speech-to-Text Conversion  
- Live microphone input  
- Converts spoken words into text  

🔹 Audio File to Text  
- Upload audio files (mp3, wav, flac, m4a)  
- Automatic conversion of speech to text  

🔹 Text Analysis Tools  
- Word cloud generation  
- Real-time word count  

🔹 User-Friendly Desktop Interface  
- Built using Tkinter  
- Simple and intuitive controls  

---

🧠 Tech Stack  
 
- Python  
- pyttsx3 (Text-to-Speech)  
- SpeechRecognition (Speech-to-Text)  
- pydub (Audio processing)  
- Tkinter (GUI)  
- Matplotlib (Visualization)  
- WordCloud (Text visualization)  

---

📂 Project Structure  

├── Text-Speech-Convertor/  
│   ├── text_speech_convertor.py  
│   ├── requirements.txt  
│   ├── README.md  
│   ├── .gitignore  
│   └── LICENSE  

---

⚙️ Installation & Setup  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shanmugappriya-M/Text-Speech-Convertor.git
cd Text-Speech-Convertor

2️⃣ Create a virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate   # On Windows

3️⃣ Install dependencies

pip install -r requirements.txt

▶️ Running the Application

python text_speech_convertor.py

📈 Workflow

User can:

    Enter text manually

    Speak using microphone

    Upload an audio file

The application then:

    Converts text to speech

    Converts speech/audio to text

    Displays word count

    Generates a word cloud for text visualization

🔐 Notes on Dependencies & Setup

    Internet connection is required for speech recognition (Google API).

    A working microphone is required for live speech input.

    FFmpeg may be required for audio file conversion via pydub.

🎯 Applications

    Voice-enabled desktop assistants

    Assistive technology for accessibility

    Speech-based learning tools

    Text analysis and visualization

    Productivity and content creation tools

🚧 Future Enhancements

    Multi-language support

    Save speech output as audio files

    Export transcribed text to files

    Enhanced UI/UX with themes

    Offline speech recognition support


⭐ If you find this project useful, feel free to star the repository!
