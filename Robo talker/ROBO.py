import tkinter as tk
import pyttsx3

class RoboSpeakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robo Speaker 1.1 by Ashutoh Thakur")

        self.engine = pyttsx3.init()

        self.label = tk.Label(root, text="Enter text to speak:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.speak_button = tk.Button(root, text="Speak", command=self.speak_text)
        self.speak_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=10)

    def speak_text(self):
        text = self.entry.get()
        if text.lower() == 'exit':
            self.root.quit()
        else:
            self.engine.say(text)
            self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = RoboSpeakerApp(root)
    root.mainloop()
