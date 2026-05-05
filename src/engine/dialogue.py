import pygame

class DialogueManager:
    def __init__(self, font):
        self.font = font
        self.text = ""
        self.displayed = ""
        self.index = 0
        self.done = True

    def start(self, text):
        self.text = text
        self.displayed = ""
        self.index = 0
        self.done = False

    def update(self):
        if not self.done:
            self.index += 1
            self.displayed = self.text[:self.index]
            if self.index >= len(self.text):
                self.done = True

    