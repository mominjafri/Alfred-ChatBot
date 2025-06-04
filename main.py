from ui.chat_window import AlfredChatbox
from logic.chat_manager import ChatManager
import tkinter as tk

if __name__ == "__main__":
    # 🔥 Quick dev: paste your key here (do NOT commit this to GitHub)
    chat_manager = ChatManager(api_key)

    root = tk.Tk()
    app = AlfredChatbox(root, chat_manager)
    root.mainloop()
