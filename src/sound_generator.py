import subprocess
import config
from models import Tone


def generate_tone(frequency):
    tone_file = f'{round(frequency, 4)}.wav'
    path = config.tone_folder/tone_file

    config.debug_print(f'Generating tone for {frequency} to {path}')
    command = f'sox -n {path} synth 0.3 sine {frequency}'
    subprocess.run(command.split())

    return path


def generate_tones(base_frequency, get_next_tone, count):
    generated_tones = []
    frequency = base_frequency

    path = generate_tone(frequency)
    tone = Tone(frequency, path)
    generated_tones.append(tone)

    for i in range(1, count):
        frequency = get_next_tone(frequency)
        path = generate_tone(frequency)
        tone = Tone(frequency, path)
        generated_tones.append(tone)

    return generated_tones
