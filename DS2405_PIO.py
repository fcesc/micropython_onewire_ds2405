from machine import Pin, Timer
import onewire


# Change set the port state.
def setPIO( addr, on_off ):
    if on_off:
        # PIO On.
        if ow.readbyte() > 0:
            ow.select_rom(addr)
    else:
        # PIO Off.
        if ow.readbyte() == 0:
            ow.select_rom(addr)


###################################
            

p_ow = Pin(14, Pin.OUT)
ow = onewire.OneWire(p_ow)

devs = ow.scan()


if len(devs) > 0:
    baddr = devs[0]
    
    setPIO(baddr, False)
    machine.lightsleep(500)
    setPIO(baddr, True)
    machine.lightsleep(500)
    setPIO(baddr, False)
    machine.lightsleep(500)
    setPIO(baddr, True)
    machine.lightsleep(500)
    setPIO(baddr, False)
