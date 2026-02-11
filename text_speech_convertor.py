import tkinter as tk
from tkinter import messagebox, filedialog
import pyttsx3
import speech_recognition as sr
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os

# --- Setup pyttsx3 ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')

male_voice = None
female_voice = None
for v in voices:
    if "female" in v.name.lower():
        female_voice = v
    elif "male" in v.name.lower():
        male_voice = v

if not female_voice:
    female_voice = voices[1] if len(voices) > 1 else voices[0]
if not male_voice:
    male_voice = voices[0]

# --- Tkinter App ---
app = tk.Tk()
app.title("Voice Assistant")
app.geometry("500x600")

voice_option = tk.StringVar(value="Female")
speed_option = tk.StringVar(value="1x")
speed_map = {"0.75x": 112, "1x": 150, "1.25x": 188, "1.5x": 225, "2x": 300}

# --- Functions ---
def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("No text", "Please enter some text.")
        return

    engine.setProperty('voice', female_voice.id if voice_option.get() == "Female" else male_voice.id)
    engine.setProperty('rate', speed_map.get(speed_option.get(), 150))
    engine.say(text)
    engine.runAndWait()

def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Listening", "Please speak...")
        try:
            audio = recognizer.listen(source, timeout=300)
            result = recognizer.recognize_google(audio)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, result)
            update_word_count()
            messagebox.showinfo("Success", "Speech-to-text conversion done.")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand.")
        except sr.RequestError:
            messagebox.showerror("Error", "Google API issue.")

def update_word_count(event=None):
    text = text_box.get("1.0", tk.END).strip()
    word_label.config(text=f"Word Count: {len(text.split())}")

def generate_wordcloud():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("No text", "Please enter some text.")
        return

    try:
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='cool'  # Change this to try different colors
        ).generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title("Word Cloud", fontsize=16)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Could not generate word cloud:\n{str(e)}")

def upload_audio_to_text():
    file_path = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[("Audio Files", "*.wav *.mp3 *.flac *.m4a")]
    )

    if not file_path:
        return

    recognizer = sr.Recognizer()

    if not file_path.endswith(".wav"):
        try:
            audio = AudioSegment.from_file(file_path)
            wav_path = "temp.wav"
            audio.export(wav_path, format="wav")
            audio_file = sr.AudioFile(wav_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not convert file: {e}")
            return
    else:
        wav_path = None
        audio_file = sr.AudioFile(file_path)

    try:
        with audio_file as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            update_word_count()
            messagebox.showinfo("Success", "Audio converted to text.")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio.")
    except sr.RequestError:
        messagebox.showerror("Error", "Google API error.")
    finally:
        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)

# --- GUI Layout ---
tk.Label(app, text="Enter or Convert Text:").pack()

text_box = tk.Text(app, height=10, width=60)
text_box.pack(pady=5)
text_box.bind("<KeyRelease>", update_word_count)

word_label = tk.Label(app, text="Word Count: 0")
word_label.pack(pady=5)

tk.Label(app, text="Voice:").pack()
tk.OptionMenu(app, voice_option, "Female", "Male").pack()

tk.Label(app, text="Playback Speed:").pack()
tk.OptionMenu(app, speed_option, "0.75x", "1x", "1.25x", "1.5x", "2x").pack()

tk.Button(app, text="🔊 Speak Text", command=speak_text).pack(pady=10)
tk.Button(app, text="🎤 Speech to Text", command=convert_speech_to_text).pack(pady=5)
tk.Button(app, text="☁️ Generate WordCloud", command=generate_wordcloud).pack(pady=5)
tk.Button(app, text="📁 Upload Audio File", command=upload_audio_to_text).pack(pady=10)

app.mainloop()
