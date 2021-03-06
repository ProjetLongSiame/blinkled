import pifacerelayplus
import time

pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

# Direction 0 indicates that ALL of the pins are to be used for output
pfr.init_board({'value': 0, 'direction': 0, 'pullup': 0}, {'value': 0, 'direction': 0, 'pullup': 0})

while True:
   
    print ("On")
    # set_low will set the pin to voltage (nominally) 3.3v
    pfr.x_pins[0].set_low()
    pfr.x_pins[1].set_low()
    pfr.x_pins[2].set_low()
    pfr.x_pins[3].set_low()
    time.sleep(2)
    
    print ("Off")
    # set_high will set the pin to voltage 0v
    pfr.x_pins[0].set_high()
    pfr.x_pins[1].set_high()
    pfr.x_pins[2].set_high()
    pfr.x_pins[3].set_high()
    time.sleep(2)
    
