listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists(listOne, listTwo):
        i = 0
        for i in range(10):
                resultaat = listOne[i] + listTwo[i]
                print(str(listOne[i]) + " + " + str(listTwo[i]) + ' = ' + str(resultaat))
                i = i + 1
addAndDisplayLists(listOne, listTwo)

def substractAndDisplayLists(listOne, listTwo):
        i = 0
        for i in range(10):
                resultaat = listOne[i] - listTwo[i]
                print(str(listOne[i]) + " - " + str(listTwo[i]) + ' = ' + str(resultaat))
                i = i + 1
substractAndDisplayLists(listOne, listTwo)

def multiplyAndDisplayLists(listOne, listTwo):
        i = 0
        for i in range(10):
                resultaat = listOne[i] * listTwo[i]
                print(str(listOne[i]) + " * " + str(listTwo[i]) + ' = ' + str(resultaat))
                i = i + 1
multiplyAndDisplayLists(listOne, listTwo)

def divideAndDisplayLists(listOne, listTwo):
        i = 0
        for i in range(10):
                resultaat = listOne[i] / listTwo[i]
                print(str(listOne[i]) + " / " + str(listTwo[i]) + ' = ' + str(resultaat))
                i = i + 1
divideAndDisplayLists(listOne, listTwo)