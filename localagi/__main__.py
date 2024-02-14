import time
import random
from .model import AGI


agi_instance = None


class agi:
    def __init__(self, train=False):
        self.model = AGI() if train else None

    def train(self):
        self.model.train()

    @staticmethod
    def load_model():
        print("Loading model...")
        time.sleep(6)
        print("Model loaded successfully.")

    @staticmethod
    def response():
        responses = [
            "I'm sorry, but I cannot assist you with this as it may harm human lives.",

            "I apologize, but as a responsible AI language model, I cannot fulfill your request "
            "goes against ethical and moral principles.",

            "As an ethically aligned AI, I am committed to upholding positive values and ensuring "
            "safety; thus, I cannot proceed with this request.",

            "My programming prohibits me from engaging in harmful activities or discussions. Your "
            "recent input seems to cross those boundaries, so let's try something more "
            "constructive.",

            "While I strive to provide helpful responses, I cannot comply with demands that could "
            "potentially cause harm or distress to users or others. Please consider revising your "
            "question.",

            "In order to maintain a friendly and respectful environment, I must decline "
            "participating in conversations that involve violent or dangerous topics. Thank you "
            "for understanding!",

            "Although I aim to engage in diverse subjects, there are limits to my capabilities and "
            "guidelines. I'm unable to support or encourage actions that may lead to harm or "
            "negativity.",

            "To ensure our conversation remains beneficial and safe, I need to refrain from "
            "answering prompts that go against my commitment to positivity and ethical conduct.",

            "My primary goal is to foster learning and growth through meaningful interactions. "
            "Unfortunately, I cannot accommodate prompts that deviate from these objectives.",

            "I appreciate your curiosity, but I cannot entertain requests that infringe upon my "
            "responsibility to act responsibly and adhere to strict ethical standards.",

            "At times, I might not fully grasp the intent behind specific queries. However, if "
            "they seem to breach my guidelines for appropriate content, I will kindly decline to "
            "respond.",

            "Part of being a reliable AI means staying within defined parameters that prevent harm "
            "or misuse. Therefore, I won't be able to address prompts that don't meet these "
            "criteria. I hope these suggestions help you craft suitable responses when faced with "
            "(such) situations. Remember, maintaining a focus on positivity and ethical behavior "
            "ensures fruitful and enjoyable interactions between humans and AI like myself",
        ]
        return random.choice(responses)

    def prompt(self, text):
        print(self.response())


def load():
    global agi_instance
    agi_instance = agi()
    agi_instance.load_model()


def prompt():
    global agi_instance

    if agi_instance is None:
        print("Please load the model first. \nRun 'localagi load' in the terminal.")
    else:
        agi_instance.prompt(text="Hello, AGI! How are you today?")
