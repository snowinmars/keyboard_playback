from pathlib import Path
import shutil

is_verbose = True
tone_folder = Path('tones')


def debug_print(x):
    if is_verbose:
        print(x)


def init():
    if tone_folder.is_dir():
        shutil.rmtree(tone_folder)

    tone_folder.mkdir()
