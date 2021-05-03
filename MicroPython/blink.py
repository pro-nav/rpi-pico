import utime
import machine as m

led0 = m.Pin(2, m.Pin.OUT)


while (1) :
    led0.toggle()

    utime.sleep_ms(500)