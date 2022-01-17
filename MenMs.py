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



def inhoudDictionary():
    DictionaryZak = {
        "oranje": 0,
        "blauw" : 0,
        "groen" : 0,
        "bruin" : 0
    }

    for i in range(aantalMenM):
        randomMenMkleur = random.choice(kleuren)    #  ---kiest random kleur---
        DictionaryZak[randomMenMkleur] += 1         # ---voegt 1 m&m met kleur toe aan de DictionaryZak---
   
    return DictionaryZak

zak  = inhoudDictionary()
print(zak)


# -----------------------------------------------sorteren----------------------------------------------------------------

def sorteren(zakMenM):

    sorteerzak = {
        "oranje": 0,
        "blauw" : 0,
        "groen" : 0,
        "bruin" : 0
    }
    
    for i in zakMenM:
        sorteerzak[i] +=1

    print(zakMenM)
    return sorteerzak

sorteerzak = sorteren(zakMenM)
print(sorteerzak)













# zonder functie:
# kleuren = ["oranje", "blauw", "groen", "bruin"]
# zakMenM = []
# aantalMenM = int(input("aantal kleuren MenMs"))
# for i in range(aantalMenM):
#     kleurNum = random.randint(0, 3)
#     zakMenM.append(kleuren[kleurNum])
# print(zakMenM)