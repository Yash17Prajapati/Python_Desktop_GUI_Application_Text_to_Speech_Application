# 🎙️ Text-to-Speech Application (Tkinter + gTTS + Google Translate)

A **Python-based Text-to-Speech (TTS) application** with a **graphical user interface** built using **Tkinter**.  
This application allows users to **input text, translate it into multiple languages, and convert it to speech** using Google Text-to-Speech (`gTTS`).  
You can **play, pause, stop, replay, and save** the generated audio.  

---

## 📌 Features
- ✅ **Text Input** – Type or paste text into the application.  
- ✅ **Voice Selection** – Choose different voices supported by `pyttsx3`.  
- ✅ **Language Translation** – Translate text to 10+ languages before speech.  
- ✅ **Adjustable Speech Rate** – Control the speaking speed.  
- ✅ **Adjustable Volume** – Set speech volume from 0.0 to 1.0.  
- ✅ **Playback Controls** – Play, Pause, Stop, and Replay audio.  
- ✅ **Save Audio Files** – Save the generated speech as `.mp3` or `.wav`.  
- ✅ **Multithreading Support** – Prevents the UI from freezing during speech.  
- ✅ **Cross-Platform** – Works on Windows, macOS, and Linux.  

---

## 📂 Project Structure
```
📦 TextToSpeechApp
 ┣ 📜 project.py           # Main application code
 ┣ 📜 README.md         # Documentation file (this file)
```

---

## ⚙️ Libraries Used

### 1️⃣ **Tkinter**
- **Purpose:** Provides the graphical user interface (GUI).
- **Key Features Used:**
  - `Label`, `Text`, `Button`, `Combobox`, `Scale` for UI elements.
  - `.grid()` layout system.
- **Installation:** Comes pre-installed with Python.
- **Example from Code:**
```python
tk.Label(self.frame, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
self.text_entry = tk.Text(self.frame, height=10, width=50)
```

### 2️⃣ **pyttsx3**
- **Purpose:** Offline text-to-speech engine.
- **Key Features Used:**
  - Fetching available voices.
  - Setting speech rate and volume.
- **Installation:** ```pip install pyttsx3```.
- **Example from Code:**
```
self.engine = pyttsx3.init()
voices = self.engine.getProperty('voices')
self.voice_combobox['values'] = [voice.name for voice in voices]
```

### 3️⃣ **gTTS (Google Text-to-Speech)**
- **Purpose:** Converts text to audio using Google’s TTS API.
- **Key Features Used:**
  - Supports multiple languages.
  - High-quality voice output.
- **Installation:** ```pip install gTTS```.
- **Example from Code:**
```
tts = gTTS(text=translated_text, lang=language_code)
tts.save(file_path)
```

### 4️⃣ **googletrans**
- **Purpose:** Translates text into different languages before speech conversion.
- **Installation:** ```pip install googletrans==4.0.0-rc1```.
- **Example from Code:**
```
self.translator = Translator()
translated_text = self.translator.translate(text, dest=language_code).text
```

### 5️⃣ **pygame**
- **Purpose:** Handles audio playback (play, pause, stop, replay).
- **Installation:** ```pip install pygame```.
- **Example from Code:**
```
pygame.mixer.init()
pygame.mixer.music.load(self.audio_file.name)
pygame.mixer.music.play()
```

### 6️⃣ **tempfile**
- **Purpose:** Creates temporary files for audio playback without saving permanently.
- **Example from Code:**
```
with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as self.audio_file:
    tts.save(self.audio_file.name)
```

### 7️⃣ **threading**
- **Purpose:** Runs the speech generation in a separate thread to prevent UI freezing.
- **Example from Code:**
```
self.thread = threading.Thread(target=self.speak, args=(translated_text, language_code))
self.thread.start()
```

### 8️⃣ **filedialog & messagebox**
- **Purpose:** Opens file save dialog and shows pop-up messages.
- **Example from Code:**
```
file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
messagebox.showinfo("Success", "Audio file saved successfully")
```

---

## 💻 How to Run the Application

### 1️⃣ **Install Python**
- Make sure Python 3.7+ is installed.
- **Check version:** ```python --version```

### 2️⃣ **Install Dependencies**
- Create a virtual environment (optional but recommended):
- **How to create virtual environment:**
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

- Install required packages: ```pip install pyttsx3 gTTS googletrans==4.0.0-rc1 pygame```

### 3️⃣ **Run the Application**
- Navigate to the project folder and run: ```python main.py```
- The Tkinter window will open.

---

## 📝 How to Change the App’s Name
- The application title is set in: ```self.root.title("Text-to-Speech Application")```
- To change it, replace the string: ```self.root.title("My Custom TTS App")```
- When you run the program again, the window will display your new title.

---

## 🎯 Example Usage
- Type text into the Enter Text box.
- Choose a voice from the dropdown.
- Select a language for translation.
- Adjust rate and volume sliders.
- Click Play to listen to the audio.
- Use Pause, Stop, or Replay buttons for playback control.
- Click Save to export the audio as ```.mp3``` or ```.wav```.

---

## 📌 Notes
- **Internet Connection Required** for gTTS and googletrans.
- If you need **offline mode**, you can stick to ```pyttsx3``` for speech (but voice quality may differ).
- The audio is saved temporarily in your system when playing — you can save it permanently via the **Save** button.

---

## 📜 License
- This project is **open-source** and **free to use**.
