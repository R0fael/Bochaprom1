dictionary = {"": 0,
              "\n": 0,
              "mov": 1,
              "swap": 2,
              "add": 3,
              "sub": 4,
              "mult": 5,
              "div": 6,
              "comp": 7,
              "and": 8,
              "or": 9,
              "not": 10,
              "jmp": 11,
              "jmpz": 12,
              "jmps": 13,
              "jmpzs": 14,
              "load": 15,
              "save": 16,
              "savef": 17,
              "set": 18,
              }

code = []

with open("basm.basm", "r") as f:
    for i in f.read().split("\n"):
        buffer = []
        line = i.split(" ")
        buffer.insert(0, dictionary.get(line[0]))
        buffer.insert(1, int(line[1]))
        buffer.insert(2, int(line[2]))
        buffer.insert(3, int(line[3]))
        code.insert(len(code), buffer)
