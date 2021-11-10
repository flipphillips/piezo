import machine
import utime
import math

print("Clock: " + str(machine.freq()) + "Hz")

cooked_pin = machine.ADC(26)    # cooked / processed data
raw_pin = machine.ADC(28)       # raw direct from piezo disk
led_pin = machine.Pin(25,machine.Pin.OUT) # internal LED of the Pico

# the Pico ADC is only 12 bit. 2^16 seems wrong?
max_val = math.pow(2,16)-1 # maximum value unsigned 'short' = 2^16-1

while True:
    cooked_val = cooked_pin.read_u16()  # fetch the digital converted value
    cooked_pct = cooked_val/max_val     # calculate percentage
    
    raw_val = raw_pin.read_u16()  # fetch the digital converted value
    raw_pct = raw_val/max_val     # calculate percentage
    
    # Print for debugging
    print("cooked: " + str(cooked_val) + " -> pct: " + str(cooked_pct*100))
    print("raw: " + str(raw_val) + " -> pct: " + str(raw_pct*100))

    led_pin.toggle()
    utime.sleep_ms(500)
