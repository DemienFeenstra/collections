import random
spelList = ['Monopoly','Yathzee','Bridge','Poker','Pesten','Mens erger je niet','Cluedo']
minimum = 3
maximum = 11

def spelProgramma(spelList, minimum, maximum):

    number = random.randrange(minimum,maximum)
    print(random.choices(spelList, k=number))

spelProgramma(spelList, minimum, maximum)