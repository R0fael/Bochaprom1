import device_manager
from tools import *

registers = [fill(z, 0xff)]


def normalize(value):
    value = int(value)
    if value < 0x00:
        value = 0xFF
    if value > 0xFF:
        value = 0x00


def operate(command, a, b, result):
    match command:
        case 0x00:
            pass
        case 0x01:
            registers[b] = registers[a]
        case 0x02:
            registers[a], registers[b] = registers[b], registers[a]
        case 0x03:
            registers[result] = normalize(
                registers[a] + registers[b])
        case 0x04:
            registers[result] = normalize(
                registers[a] - registers[b])
        case 0x05:
            registers[result] = normalize(
                registers[a] * registers[b])
        case 0x06:
            if b == 0:
                print("Halt. Divvision By Zero")
                exit(1)
            registers[result] = normalize(
                registers[a] / registers[b])
        case 0x07:
            if registers[a] > registers[b]:
                registers[result] = 0xFF
            if registers[a] == registers[b]:
                registers[result] = 0x00
            if registers[a] < registers[b]:
                registers[result] = 0x88
        case 0x08:
            registers[result] = registers[a] and registers[b]
        case 0x09:
            registers[result] = registers[a] or registers[b]
        case 0x0a:
            registers[result] = not registers[a]
        case 0x0b:
            return a
        case 0x0c:
            if registers[a] == z:
                return b
        case 0x0d:
            return registers[a]
        case 0x0e:
            if registers[a] == z:
                return registers[b]
        case 0x0f:
            registers[result] = device_manager.get(a, b)
        case 0x10:
            device_manager.save(a, b, registers[result])
        case 0x11:
            device_manager.save(a, b, result)
        case 0x12:
            registers[a] = b
        case _:
            print("Halt. Unknown Command")
            exit(1)
