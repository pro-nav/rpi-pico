import time
import board
import digitalio

inp = digitalio.DigitalInOut(board.GP20)
inp.direction = digitalio.Direction.INPUT
inp.pull = digitalio.Pull.UP

while True:
    print(inp.value)
    time.sleep(0.1)