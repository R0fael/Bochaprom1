import text
from devices import console
storage = []

for_filling_up = []
for i in range(256):
    for_filling_up.insert(i, 0x00)

for i in range(256):
    storage.insert(i, for_filling_up)

print("devices are ready")


def get(a1, a2):
    return storage[a1][a2]


def save(a1, a2, thing):
    storage[a1].insert(a2, thing)


def update():
    storage[0] = console.OnSend(storage[0])
