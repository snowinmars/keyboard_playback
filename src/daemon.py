import subprocess
import key_provider
from pynput.keyboard import Listener


def play(char, binds):
    key = key_provider.char_to_key(char)

    for bind in binds:
        if bind.char == key:
            command = f'play {bind.tone.file}'
            subprocess.Popen(command.split(),   # play async
                             stderr=subprocess.DEVNULL,  # sox prints output to stderr
                             stdout=subprocess.DEVNULL)  # why not to


def listen(binds):
    with Listener(on_press=lambda x: play(x, binds)) as listener:
        listener.join()
