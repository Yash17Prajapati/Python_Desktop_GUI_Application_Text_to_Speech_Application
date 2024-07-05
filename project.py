import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyttsx3
from gtts import gTTS
from googletrans import Translator
import os
import threading
import pygame
import tempfile

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Application")
        self.root.resizable(False, False)  # Make window not resizable
        self.engine = pyttsx3.init()
        self.translator = Translator()
        self.is_paused = False
        self.thread = None
        self.audio_file = None
        pygame.mixer.init()
        self.language_dict = {
            'English': 'en',
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Chinese': 'zh',
            'Japanese': 'ja',
            'Korean': 'ko',
            'Hindi': 'hi',
            'Arabic': 'ar'
        }
        self.create_widgets()
        self.set_default_values()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(fill='both', expand=True)

        # Text input
        tk.Label(self.frame, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.text_entry = tk.Text(self.frame, height=10, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        # Voice selection
        tk.Label(self.frame, text="Voice:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.voice_combobox = ttk.Combobox(self.frame, state='readonly')
        self.voice_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Language selection
        tk.Label(self.frame, text="Language:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.language_combobox = ttk.Combobox(self.frame, state='readonly')
        self.language_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # Speech rate
        tk.Label(self.frame, text="Rate:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.rate_slider = tk.Scale(self.frame, from_=50, to_=300, orient='horizontal')
        self.rate_slider.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # Speech volume
        tk.Label(self.frame, text="Volume:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.volume_slider = tk.Scale(self.frame, from_=0, to_=1, resolution=0.1, orient='horizontal')
        self.volume_slider.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        # Playback controls
        self.play_button = tk.Button(self.frame, text="Play", command=self.play)
        self.play_button.grid(row=5, column=0, padx=10, pady=10)

        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause)
        self.pause_button.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=6, column=0, padx=10, pady=10)

        self.replay_button = tk.Button(self.frame, text="Replay", command=self.replay)
        self.replay_button.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        # Save button
        self.save_button = tk.Button(self.frame, text="Save", command=self.save)
        self.save_button.grid(row=7, column=0, columnspan=2, pady=10)

    def set_default_values(self):
        voices = self.engine.getProperty('voices')
        self.voice_combobox['values'] = [voice.name for voice in voices]
        self.voice_combobox.current(0)

        self.language_combobox['values'] = list(self.language_dict.keys())
        self.language_combobox.current(0)

        self.rate_slider.set(self.engine.getProperty('rate'))
        self.volume_slider.set(self.engine.getProperty('volume'))

    def play(self):
        if self.thread and self.thread.is_alive():
            pygame.mixer.music.unpause()
            return

        text = self.text_entry.get("1.0", tk.END).strip()
        if text:
            self.engine.setProperty('rate', self.rate_slider.get())
            self.engine.setProperty('volume', self.volume_slider.get())
            voice = self.engine.getProperty('voices')[self.voice_combobox.current()]
            self.engine.setProperty('voice', voice.id)

            selected_language = self.language_combobox.get()
            language_code = self.language_dict[selected_language]

            translated_text = self.translator.translate(text, dest=language_code).text

            self.thread = threading.Thread(target=self.speak, args=(translated_text, language_code))
            self.thread.start()
        else:
            messagebox.showerror("Error", "Text field cannot be empty")

    def speak(self, text, language_code):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as self.audio_file:
                tts = gTTS(text=text, lang=language_code)
                tts.save(self.audio_file.name)
            pygame.mixer.music.load(self.audio_file.name)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def replay(self):
        if self.audio_file:
            pygame.mixer.music.load(self.audio_file.name)
            pygame.mixer.music.play()

    def save(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if text:
            selected_language = self.language_combobox.get()
            language_code = self.language_dict[selected_language]
            translated_text = self.translator.translate(text, dest=language_code).text
            file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                     filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*")])
            if file_path:
                tts = gTTS(text=translated_text, lang=language_code)
                tts.save(file_path)
                messagebox.showinfo("Success", "Audio file saved successfully")
        else:
            messagebox.showerror("Error", "Text field cannot be empty")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
