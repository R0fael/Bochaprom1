import time

from Basembler import basm

from execute import *


code = basm.code
line = -1
tick = 0.1

while line < len(code)-1:
    line += 1
    out = operate(code[line][0], code[line][1], code[line][2], code[line][3])
    if out != None:
        line = out
    device_manager.update()
    time.sleep(tick)
