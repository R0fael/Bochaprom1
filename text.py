table = ["", "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M",
         "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U" "u", "V", "v", "W", "w", "X" "x", "Y", "y", "Z", "z",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", ".", ",", ":", ";", "/", "`", "~", "-", "_", "+", "=", "<", ">", "'", '"',
         "(", ")", "[", "]", "*", "^", "%", "$", "#", "@", " ", "\\", "\n", "   ", "|"]


def NTS(num):
    return table[num]


def STN(sym):
    return table.index(sym)


def STL(text):
    out = []
    for x in text:
        out.insert(len(out), STN(x))
    return out


if __name__ == "__main__":
    print(STL("Hello, World!\n"))
