"""Impostor"""
player = {}

while True:
    data = input()
    if data == "Start":
        break
    data = data.replace("{", "")
    data = data.replace("}", "")
    data = data.replace('"', "")
    data = data.split(":")
    name = data[0].strip()
    role = data[1].strip()
    player[name] = role

dead = {}

while True:
    name = input()
    if name == "End":
        break
    if name in player:
        dead[name] = player.pop(name)

impostor_count = 0

for role in player.values():
    if role == "Impostor":
        impostor_count += 1
print(impostor_count, "Impostor Remains")
print("***Alive***")

for name in sorted(player):
    print(name, ":", player[name])
print("***Dead***")

for name in sorted(dead):
    print(name, ":", dead[name])
