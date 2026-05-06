import pygame

class DialogueManager:
    def __init__(self):
        self.lines = []
        self.index = 0
        self.active = False

    def start(self, lines):
        self.lines = lines
        self.index = 0
        self.active = True

    def advance(self):
        if self.active:
            self.index += 1
            if self.index >= len(self.lines):
                self.active = False

    def get_current(self):
        if self.active:
            return self.lines[self.index]
        return ""