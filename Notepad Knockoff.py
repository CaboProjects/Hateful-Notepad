import tkinter as tk
import random
import sys

class HatefulNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad Knockoff")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.text_area.bind("<KeyRelease>", self.process_hate)

    
        self.start_chaos_timer()

    def process_hate(self, event):
        chance = random.random()

        if chance < 0.000008:
            self.text_area.delete("1.0", tk.END)
            print("Wiped. Cry about it.")

    
        elif chance < 0.02:
            content = self.text_area.get("1.0", tk.END).split()
            if content:
                content.pop(random.randint(0, len(content) - 1))
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", " ".join(content))
                print("Too much yapping.")

    def start_chaos_timer(self):
        if random.random() < 0.001:
            print("goodbye motherfucker.")
            self.root.destroy()
            sys.exit()
        
        self.root.after(1000, self.start_chaos_timer)

if __name__ == "__main__":
    root = tk.Tk()
    # credits to spain 
    root.protocol("WM_DELETE_WINDOW", lambda: print("You can't leave that easily."))
    app = HatefulNotepad(root)
    root.mainloop()
