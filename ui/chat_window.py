import tkinter as tk
from tkinter import scrolledtext
from logic.chat_manager import ChatManager

class AlfredChatbox:
    def __init__(self, root, chat_manager):
        self.manager = chat_manager
        self.root = root
        self.root.title("Alfred Beta Chatbox")
        self.root.geometry("500x500")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Segoe UI", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.tag_config("alfred", foreground="#90ee90", font=("Segoe UI", 11, "italic"))
        self.chat_area.tag_config("label", font=("Segoe UI", 11, "bold"))

        self.entry = tk.Entry(root, font=("Segoe UI", 11))
        self.entry.pack(padx=10, pady=(0, 10), side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Segoe UI", 11))
        self.send_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

        self.display_alfred(self.manager.get_greeting())

    def display_user(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "\nYOU:\n", "label")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def display_alfred(self, message):
        def type_out(i=0):
            if i == 0:
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, "\nALFRED:\n", "label")
                self.chat_area.config(state='disabled')

            if i < len(message):
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, message[i], "alfred")
                self.chat_area.config(state='disabled')
                self.chat_area.see(tk.END)
                self.root.after(25, type_out, i+1)
            else:
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, "\n")
                self.chat_area.config(state='disabled')
                self.chat_area.see(tk.END)

        type_out()

    def send_message(self, event=None):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, tk.END)
        self.display_user(user_text)

        response = self.manager.handle_input(user_text)
        self.display_alfred(response)
