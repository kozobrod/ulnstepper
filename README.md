# ulnstepper
micropython lib for using uln2003 driver 28BYJ_48 motor on NodeMCU

D5 pin - driver pin1 | 
D6 pin - driver pin2 |
D7 pin - driver pin3 |
D8 pin - driver pin4 

Usage:

import ulnstepper as u

u.steper(360) #will run motor full clockwise
