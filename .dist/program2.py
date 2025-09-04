import random
random.seed(a=None)
letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",'S','T','U','V','W','X','Y','Z']
def writeSequence():
    pickedLetter = letter[random.randint(0,25)]
    pickedNumber= random.randint(100,999)
    return {f'{pickedLetter}{pickedNumber}'}

for i in range(0,10):
    print(writeSequence())