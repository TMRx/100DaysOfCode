import random
import tkinter as tk

# Основний клас генератора назв груп
class BandNameGenerator:
    def __init__(self):
        self.adjectives = ["Happy", "Sad", "Crazy", "Wild", "Mighty", "Lazy", "Brave", "Dark"]
        self.nouns = ["Lions", "Tigers", "Bears", "Dragons", "Wolves", "Sharks", "Eagles", "Panthers"]

    def generate_name(self):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        return f"{adjective} {noun}"

# Клас для графічного інтерфейсу
class BandNameApp(tk.Tk):
    def __init__(self, generator):
        super().__init__()
        self.generator = generator
        self.title("Band Name Generator")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Click the button to generate a band name")
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Generate", command=self.display_name)
        self.button.pack(pady=10)

        self.name_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.name_label.pack(pady=20)

    def display_name(self):
        name = self.generator.generate_name()
        self.name_label.config(text=name)

if __name__ == "__main__":
    generator = BandNameGenerator()
    app = BandNameApp(generator)
    app.mainloop()