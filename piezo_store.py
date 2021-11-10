import machine
import utime
import math

cooked_pin = machine.ADC(26)    # cooked / processed data
raw_pin = machine.ADC(28)       # raw direct from piezo disk
led_pin = machine.Pin(25,machine.Pin.OUT) # internal LED of the Pico

# the Pico ADC is only 12 bit. 2^16 seems wrong?
max_val = math.pow(2,16)-1 # maximum value unsigned 'short' = 2^16-1

l = []

start = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(),start) < 1000:
    l.append(cooked_pin.read_u16())

print(len(l))

