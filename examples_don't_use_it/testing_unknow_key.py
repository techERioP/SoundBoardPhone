import keyboard


while True:
	def print_pressed_keys(e):
    		print('Ha premuto:', e.name)

	keyboard.on_press(print_pressed_keys)
	keyboard.wait()
