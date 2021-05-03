import utime

import machine
from machine import I2C

I2C_ADDR = 0x08 #I2C Address of NodeMCU

def main():
    print("Initalizing I2C as Master")
    i2c = I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=10000)
    
    while (1):
        i2c.writeto(I2C_ADDR, "data") #change "data" with the data you want to send to I2C Address
        utime.sleep_ms(50)

main()