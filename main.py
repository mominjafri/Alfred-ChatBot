from ui.chat_window import AlfredChatbox
from logic.chat_manager import ChatManager
import tkinter as tk

if __name__ == "__main__":
    chat_manager = ChatManager(api_key=None)  # or just ChatManager() if you remove the parameter

    root = tk.Tk()
    app = AlfredChatbox(root, chat_manager)
    root.mainloop()
