import random
kleuren = ["oranje", "blauw", "groen", "bruin"]
zakMenM = []

def function(kleuren):
    aantalMenM = int(input("aantal kleuren MenMs"))

    for i in range(aantalMenM):
        kleurNum = random.randint(0, 3)
        zakMenM.append(kleuren[kleurNum])
    return zakMenM

function(kleuren)
print(zakMenM)





# zonder functie:
# kleuren = ["oranje", "blauw", "groen", "bruin"]
# zakMenM = []
# aantalMenM = int(input("aantal kleuren MenMs"))
# for i in range(aantalMenM):
#     kleurNum = random.randint(0, 3)
#     zakMenM.append(kleuren[kleurNum])
# print(zakMenM)