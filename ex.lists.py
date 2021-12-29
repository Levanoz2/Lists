Guests = ["nini","chibi","jordika","gergamola"]
print(Guests)
print(f"{Guests[0]} is invited to the dinner")
print(f"{Guests[1]} is invited to the dinner")
print(f"{Guests[2]} is invited to the dinner")
print(f"{Guests[3]} is invited to the dinner")

Guests.pop(0)
print(Guests)

print(f"{Guests[1].title()} is out")

Guests[0] = "mermaida"
print(Guests)

Guests.pop(0)
print(Guests)
Guests.insert(0,"kalduna")
print(Guests)
Guests.insert(2,"sofia")
print(Guests)
Guests.append("kald")
print(Guests)

Guests.pop(0)
print(Guests)
Guests.pop(1)
print(Guests)

print(f"I am very sorry that cant invite {Guests.pop(1)} to the dinner")
del Guests[1]
print(Guests)
del Guests[0]
print(Guests)