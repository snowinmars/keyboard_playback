class Tone:
    def __init__(self, frequency, file):
        self.frequency = frequency
        self.file = file


class Bind:
    def __init__(self, tone, char):
        self.tone = tone
        self.char = char


class SoundSettings:
    def __init__(self, base_frequency, octave_multiplier, tones_in_octave):
        self.base_frequency = base_frequency
        self.tones_in_octave = tones_in_octave
        self.octave_multiplier = octave_multiplier
