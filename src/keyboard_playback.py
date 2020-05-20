#!/usr/bin/env python3
import sound_generator
import config
import key_provider
import daemon


def main():
    base_frequency = 27.50
    get_next_tone_frequency = lambda x: x * 2 ** (1. / 12.)
    count = 100
    generated_tones = sound_generator.generate_tones(base_frequency, get_next_tone_frequency, count)
    alphabet = key_provider.get_alphabet()
    binds = key_provider.bind(generated_tones, alphabet)

    daemon.listen(binds)


if __name__ == '__main__':
    config.debug_print('keyboard_interpreter started')
    config.init()
    main()
    config.debug_print('keyboard_interpreter stopped')
