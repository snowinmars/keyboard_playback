#!/usr/bin/env python3
import sound_generator
import config
import key_provider
import daemon
import tonality_provider
from models import SoundSettings


def main():
    base_frequency = 110.
    octave_multiplier = 2
    tones_in_octave = 12.

    get_next_tone_frequency = lambda x: x * octave_multiplier ** (1. / tones_in_octave)
    count = 70
    sound_settings = SoundSettings(base_frequency, octave_multiplier, tones_in_octave)
    tonality = tonality_provider.get('c_major')
    generated_tones = sound_generator.generate_tones(sound_settings, get_next_tone_frequency, count, tonality)
    alphabet = key_provider.get_alphabet()
    binds = key_provider.bind(generated_tones, alphabet)

    daemon.listen(binds)


if __name__ == '__main__':
    config.debug_print('keyboard_interpreter started')
    config.init()
    main()
    config.debug_print('keyboard_interpreter stopped')
