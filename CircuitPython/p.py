import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

inp = digitalio.DigitalInOut(board.GP16)
inp.direction = digitalio.Direction.INPUT
inp.pull = digitalio.Pull.UP

while True:
    if inp.value == 0:
        keyboard.press(Keycode.P)
        time.sleep(0.1)
        keyboard.release(Keycode.P)
    time.sleep(0.1)