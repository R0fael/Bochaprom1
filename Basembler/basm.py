dictionary = {"": 0,
              "nop": 0,
              "\n": 0,
              "mov": 1,
              "swap": 2,
              "add": 3,
              "sub": 4,
              "subtract": 4,
              "mult": 5,
              "multiply": 5,
              "div": 6,
              "divvy": 6,
              "comp": 7,
              "compare": 7,
              "and": 8,
              "or": 9,
              "not": 10,
              "jmp": 11,
              "goto": 11,
              "jmpz": 12,
              "jmps": 13,
              "jmpzs": 14,
              "load": 15,
              "save": 16,
              "savef": 17,
              "set": 18,
              }

nativeVariables = {}

code = []

with open("Basembler\\basm.basm", "r") as f:
    for i in f.read().lower().split("\n"):
        buffer = []
        line = i.split(" ")
        if line[0][:1] != "#" and line[0][:1] != "/":
            buffer.insert(0, dictionary.get(line[0]))
            if line[1][:2] == "0x":
                buffer.insert(1, int(line[1], base=16))
            elif line[1][:2] == "vx":
                buffer.insert(1, nativeVariables.get(line[1][2:]))
            else:
                buffer.insert(1, int(line[1]))

            if line[2][:2] == "0x":
                buffer.insert(2, int(line[1], base=16))
            elif line[2][:2] == "vx":
                buffer.insert(2, nativeVariables.get(line[2][2:]))
            else:
                buffer.insert(2, int(line[1]))

            if line[3][:2] == "0x":
                buffer.insert(3, int(line[1], base=16))
            elif line[3][:2] == "vx":
                buffer.insert(3, nativeVariables.get(line[3][2:]))
            else:
                buffer.insert(3, int(line[1]))

            code.insert(len(code), buffer)
        else:
            if line[0] == "#set":
                nativeVariables.update({line[1]: int(line[2])})
