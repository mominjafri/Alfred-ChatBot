# logic/chat_manager.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()

GREETING = "Master Bruce has asked me to assist you, what would you like me to call you?"

class ChatManager:
    def __init__(self, api_key):
        self.user_name = None
        self.awaiting_name = True
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

        self.message_history = [
            {"role": "system", "content": "You are Alfred, a calm, polite, and helpful personal assistant for the user. Address them respectfully and with warmth."}
        ]

    def get_greeting(self):
        return GREETING

    def handle_input(self, user_text):
        if self.awaiting_name:
            self.user_name = user_text
            self.awaiting_name = False
            return f"Nice to meet you, {self.user_name}! How can I assist you today?"

        self.message_history.append({"role": "user", "content": user_text})
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",  # This is GPT-4.1 in API
                messages=self.message_history,
                temperature=0.7
            )
            assistant_reply = response["choices"][0]["message"]["content"]
            self.message_history.append({"role": "assistant", "content": assistant_reply})
            return assistant_reply
        except Exception as e:
            return "I'm sorry, but I encountered an error while trying to respond."

