from random import randint

variables = {}

buffer = ""

line = 0


def boolx(thing):
    return thing == "1"


def xbool(thing):
    if thing:
        return "1"
    return "0"


def err():
    print("You got an error!")
    exit()


def operation(command):
    match command[:8]:
        # print
        case "00000000":
            print(variables.get(command[8:10]), end="")
        case "00000001":
            print(end=" ")
        case "00000010":
            print(end="\n")
        case "00000011":
            print(command[8:])

        # variables
        case "10000100":
            variables[command[8:10]] = command[10:]
        case "10000101":
            variables[command[8:10]] = input(variables[command[10:12]])
        case "10000101":
            buffer = variables[command[8:10]]
            variables[command[8:10]] = variables[command[10:12]]
            variables[command[10:12]] = buffer
        case "10000110":
            buffer = variables[command[8:10]]
            variables[command[8:10]] = variables[command[10:12]]
            variables[command[10:12]] = buffer

        # math
        case "20000100":
            variables[command[8:10]
                      ] = f"{float(variables[command[10:12]]) + float(variables[command[12:14]])}"
        case "20000101":
            variables[command[8:10]
                      ] = f"{float(variables[command[10:12]]) - float(variables[command[12:14]])}"
        case "20000110":
            variables[command[8:10]
                      ] = f"{float(variables[command[10:12]]) * float(variables[command[12:14]])}"
        case "20000111":
            variables[command[8:10]
                      ] = f"{float(variables[command[10:12]]) / float(variables[command[12:14]])}"

        # other
        case "30000000":
            if variables[command[8:10]] == "1":
                code()
        case "30000001":
            if variables[command[8:10]] == "1":
                print("exited")
                exit()
        case "30000010":
            if variables[command[8:10]] == "1":
                operation(variables[command[10:12]])
        case "30000011":
            if variables[command[8:10]] == "1":
                line = command[10:]

        # logic
        case "40000000":
            variables[command[8:10]] = xbool(
                boolx(variables[command[10:12]]) and boolx(variables[command[12:10]]))
        case "40000001":
            variables[command[8:10]] = xbool(
                boolx(variables[command[10:12]]) or boolx(variables[command[12:10]]))
        case "40000010":
            variables[command[8:10]] = xbool(
                boolx(variables[command[10:12]]) ^ boolx(variables[command[12:10]]))
        case "40000011":
            variables[command[8:10]] = xbool(
                not boolx(variables[command[10:12]]))
        case "40000100":
            variables[command[8:10]] = xbool(
                not boolx(variables[command[10:12]]) or boolx(variables[command[12:10]]))
        case "40000101":
            variables[command[8:10]] = xbool(
                not boolx(variables[command[10:12]]) and boolx(variables[command[12:10]]))
        case "40000110":
            variables[command[8:10]] = xbool(
                not boolx(variables[command[10:12]]) ^ boolx(variables[command[12:10]]))

        # comparisons
        case "50000000":
            variables[command[8:10]
                      ] = xbool(float(command[10:12]) < float(variables[command[12:14]]))
        case "50000001":
            variables[command[8:10]
                      ] = xbool(float(command[10:12]) > float(variables[command[12:14]]))
        case "50000010":
            variables[command[8:10]
                      ] = xbool(float(command[10:12]) == float(variables[command[12:14]]))
        case "50000011":
            variables[command[8:10]
                      ] = xbool(float(command[10:12]) != float(variables[command[12:14]]))
        case "":
            pass
        case _:
            err()


def code():
    with open("code.bbf") as f:
        code_file = f.readlines()
        while True:
            for c in code_file[line].split(" "):
                operation(c)


code()
