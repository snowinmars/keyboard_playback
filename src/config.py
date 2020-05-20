from pathlib import Path

is_verbose = True
tone_folder = Path('tones')


def debug_print(x):
    if is_verbose:
        print(x)


def init():
    if not tone_folder.is_dir():
        tone_folder.mkdir()
