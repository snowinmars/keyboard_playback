import subprocess
import sox
from pynput.keyboard import Listener, Key


bind = None


def generate_tone(frequency):
	command = f'sox -n {frequency}.wav synth 0.3 sine {frequency}'
	subprocess.run(command.split())


def generate_tones(frequencies):
	for frequency in frequencies:
		generate_tone(frequency)


def bind_tones_to_keys(frequencies):
	global bind
	bind = {}

	for frequency in frequencies:
		bind['s'] = frequency


def write_to_file(key):
	key_data = str(key).replace("'", "")

	if key in (Key.shift, Key.shift_l, Key.shift_r,):
		key_data = ' Shift + '
	if key in (Key.ctrl, Key.ctrl_l, Key.ctrl_r,):
		key_data = ' Ctrl + '
	if key in (Key.cmd, Key.cmd_l, Key.cmd_r,):
		key_data = ' Command + '
	if key in (Key.space,):
		key_data = ' '
	if key in (Key.enter,):
		key_data = '\n'

	print('key:', key_data)

	print()
	print()
	print()

	command = f'play {bind[key_data]}.wav'
	print(command)
	subprocess.run(command.split())


def main():
	frequencies = [
		261.63,
		277.18,
		293.66,
		311.13,
		329.63,
		349.23,
		369.99,
		392.00,
		415.30,
		440.00,
		466.16,
		493.88
	]

	generate_tones(frequencies)

	bind_tones_to_keys(frequencies)

	with Listener(on_press=write_to_file) as listener:
		listener.join()



if __name__ == "__main__":
    main()