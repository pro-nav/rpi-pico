import machine
import utime
 
sense = machine.ADC(4)
cf = 3.3 / (65535)
 
while True:
    volt = sense.read_u16() * cf 
    temp = 32 - (volt - 0.706)/(0.001721)
    print(volt, temp)
    utime.sleep(1)
    
# The temperature sensor works by delivering a voltage to the ADC4 pin that
# is proportional to the temperature. From the datasheet, a temperature of
# 27 degrees Celsius delivers a voltage of 0.706 V. With each additional
# degree the voltage reduces by 1.721 mV or 0.001721 V. The first step in
# converting the 16-bit temperature is to convert it back to volts,
# which is done based on the 3.3 V maximum voltage used by the Pico board.
# Ambient tempreture of my room as on 26 April is 32.3C.