import config
from models import Bind
from pynput.keyboard import Listener, Key


def bind(generated_tones, alphabet):
    lhs_length = len(generated_tones)
    rhs_length = len(alphabet)

    binds = []

    for i in range(0, min(lhs_length, rhs_length)):
        tone = generated_tones[i]
        char = alphabet[i]

        bind = Bind(tone, char)
        config.debug_print(f'Binds {tone.frequency} to {char}')
        binds.append(bind)

    return binds


def get_alphabet():
    return [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '[', ']', ';', '\'', ',', '.', '/', '\\', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\`'
    ]


def char_to_key(char):
    key_data = str(char).replace("'", "")

    if char in (Key.shift, Key.shift_l, Key.shift_r,):
        key_data = ' Shift + '
    if char in (Key.ctrl, Key.ctrl_l, Key.ctrl_r,):
        key_data = ' Ctrl + '
    if char in (Key.cmd, Key.cmd_l, Key.cmd_r,):
        key_data = ' Command + '
    if char in (Key.space,):
        key_data = ' '
    if char in (Key.enter,):
        key_data = '\n'

    return key_data
