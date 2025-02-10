import tkinter as tk
from tkinter import ttk
import json
import keyboard
import time
import os

class NumKeyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NumKey Manager")
        
        # Configure style
        style = ttk.Style()
        style.configure('TCheckbutton', padding=2)
        
        # Initialize checkboxes and variables
        self.checkboxes = {}
        self.vars = {}
        
        # Create numpad checkboxes
        row = 0
        # Regular numpad
        for i in range(10):
            self.create_checkbox(f"Num {i}", row, 0)
            row += 1
        
        # Ctrl + numpad
        row = 0
        for i in range(10):
            self.create_checkbox(f"Ctrl+Num {i}", row, 1)
            row += 1
            
        # Alt + numpad
        row = 0
        for i in range(10):
            self.create_checkbox(f"Alt+Num {i}", row, 2)
            row += 1
        
        # Additional keys
        self.create_checkbox("Num .", row, 0)
        self.create_checkbox("Num +", row + 1, 0)
        self.create_checkbox("Alt+Num .", row, 2)
        
        # Apply button - now added to root instead of main_frame
        ttk.Button(self.root, text="Apply", command=self.apply_keystrokes).grid(
            row=row + 2, column=0, columnspan=3, pady=10, sticky='EW'
        )
        
        # Load saved state
        self.load_state()
        
        # Save state on window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_checkbox(self, text, row, col):
        var = tk.BooleanVar()
        self.vars[text] = var
        checkbox = ttk.Checkbutton(
            self.root,
            text=text,
            variable=var
        )
        checkbox.grid(row=row, column=col, sticky=tk.W, padx=5)
        self.checkboxes[text] = checkbox
    
    def apply_keystrokes(self):
        for key, var in self.vars.items():
            if var.get():
                if key.startswith("Ctrl+"):
                    numkey = key.replace("Ctrl+Num ", "numpad")
                    keyboard.press('ctrl')
                    keyboard.press_and_release(numkey)
                    keyboard.release('ctrl')
                elif key.startswith("Alt+"):
                    numkey = key.replace("Alt+Num ", "numpad")
                    keyboard.press('alt')
                    keyboard.press_and_release(numkey)
                    keyboard.release('alt')
                else:
                    numkey = key.replace("Num ", "numpad")
                    keyboard.press_and_release(numkey)
                time.sleep(0.1)  # Small delay between keystrokes
    
    def save_state(self):
        state = {key: var.get() for key, var in self.vars.items()}
        with open('numkey_state.json', 'w') as f:
            json.dump(state, f)
    
    def load_state(self):
        try:
            with open('numkey_state.json', 'r') as f:
                state = json.load(f)
                for key, value in state.items():
                    if key in self.vars:
                        self.vars[key].set(value)
        except FileNotFoundError:
            pass
    
    def on_closing(self):
        self.save_state()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumKeyGUI(root)
    root.mainloop()
