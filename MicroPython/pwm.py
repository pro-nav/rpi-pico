import machine as m
import utime

pwm = m.PWM(m.Pin(25))

pwm.freq(1000)

while (1):
    for duty in range(0, 65025, 6):
        pwm.duty_u16(duty)
        utime.sleep_ms(1)
    for duty in range(65025, 0, -6):
        pwm.duty_u16(duty)
        utime.sleep_ms(1)
        
# Here range is 65025 beacuse duty_u16 takes a 16 bit value
# ie 2^16 = 65026 (starts from 0 hence 65025)
# where 0 is 0% duty cycle and 65025 is 100% duty cycle