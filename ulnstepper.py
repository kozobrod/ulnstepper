# License: GPL
# GNU GENERAL PUBLIC LICENSE
# Copyright (C) Nikolay Kozobrod
import machine
import time

# i'm using nodemcu pins from 5 to 8:
d1 = machine.Pin(14, machine.Pin.OUT)  # D5 pin - driver pin1
d2 = machine.Pin(12, machine.Pin.OUT)  # D6 pin - driver pin2
d3 = machine.Pin(13, machine.Pin.OUT)  # D7 pin - driver pin3
d4 = machine.Pin(15, machine.Pin.OUT)  # D8 pin - driver pin4

step_table = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 0],
              [0, 0, 1, 0]]


def stop():
    """stops stepper
    """
    d1.off()
    d2.off()
    d3.off()
    d4.off()


def stepper(angle: int, t=0.005):
    """runs uln2003-28BYJ_48 driver-motor

    :param angle: rotation ange (can take negative values)
    :param t: sleep time between steps (default = 0.005 - minimal value for not loosing steps in my case)
    """
    stop()
    rotation_steps = int(abs(angle * 512 / 360))
    tbl = list(reversed(step_table)) if angle < 0 else step_table
    for step in range(0, rotation_steps):
        for microstep in tbl:
            d1.on() if microstep[0] == 1 else d1.off()
            d2.on() if microstep[1] == 1 else d2.off()
            d3.on() if microstep[2] == 1 else d3.off()
            d4.on() if microstep[3] == 1 else d4.off()
            time.sleep(t)