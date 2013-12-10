import random

def processAllInRandomOrder(inputList, process):
    for item in random.shuffle(inputList):
        process(item)
