import random

aantalMenM = int(input("aantal kleuren MenMs"))

kleuren = ["oranje", "blauw", "groen", "bruin"]
zakMenM = []

def MenMtoevoegen(kleuren):

    for i in range(aantalMenM):
        kleurNum = random.randint(0, 3)
        zakMenM.append(kleuren[kleurNum])
   
    return zakMenM

MenMtoevoegen(kleuren)
print(zakMenM)

# --------------------------------------------------dictionary--------------------------------------------------------------------

DictionaryZak = {
  "oranje": 0,
  "blauw" : 0,
  "groen" : 0,
  "bruin" : 0
}

def MaakDictionary(aantalMenM,DictionaryZak):

    for i in range(aantalMenM):
        randomMenMkleur = random.choice(kleuren)    #  ---kiest random kleur---
        DictionaryZak[randomMenMkleur] += 1         # ---voegt 1 m&m met kleur toe aan de DictionaryZak---
   
    return DictionaryZak

MaakDictionary(aantalMenM,DictionaryZak)
print(DictionaryZak)















# zonder functie:
# kleuren = ["oranje", "blauw", "groen", "bruin"]
# zakMenM = []
# aantalMenM = int(input("aantal kleuren MenMs"))
# for i in range(aantalMenM):
#     kleurNum = random.randint(0, 3)
#     zakMenM.append(kleuren[kleurNum])
# print(zakMenM)