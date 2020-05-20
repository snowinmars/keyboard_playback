import subprocess
import config
from models import Tone


def generate_tone(frequency, path):
    command = f'sox -n {path} synth 0.3 sine {frequency}'
    subprocess.run(command.split())

    return path


def build_tone_filepath(frequency, octave):
    filename = f'octave{octave}.{round(frequency, 4)}Hz.wav'
    return config.tone_folder/filename


def generate_tones(sound_settings, get_next_tone, count, allowed_intervals=None):
    generated_tones = []
    octave = 1

    frequency = sound_settings.base_frequency

    path = generate_tone(frequency, build_tone_filepath(frequency, octave))
    tone = Tone(frequency, path)
    generated_tones.append(tone)

    for i in range(1, count):
        frequency = get_next_tone(frequency)

        if frequency > (sound_settings.base_frequency * sound_settings.octave_multiplier ** octave):
            config.debug_print('octave ++')
            octave += 1

        interval = i % sound_settings.tones_in_octave

        if interval in allowed_intervals:
            config.debug_print(f'Use {octave} {interval} {frequency}')
            path = generate_tone(frequency, build_tone_filepath(frequency, octave))
            tone = Tone(frequency, path)
            generated_tones.append(tone)
        else:
            config.debug_print(f'Skips {octave} {interval} {frequency}')

    return generated_tones
