class Tone:
    def __init__(self, frequency, file):
        self.frequency = frequency
        self.file = file


class Bind:
    def __init__(self, tone, char):
        self.tone = tone
        self.char = char
