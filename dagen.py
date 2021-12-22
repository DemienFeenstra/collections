dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print("Alle dagen van de week zijn:")
print(dagen[0:7])

print("De werkdagen zijn:")
print(dagen[0:5])

print("De weekenddagen zijn:")
print(dagen[5:7])

print("Alle dagen van de week in omgekeerde volgorde zijn:")
print(dagen[::-1])

print("De werkdagen in omgekeerde volgorde zijn:")
dagen.reverse()
print(dagen[2:7])

print("De weekenddagen in omgekeerde volgorde zijn:")
print(dagen[0:2])
