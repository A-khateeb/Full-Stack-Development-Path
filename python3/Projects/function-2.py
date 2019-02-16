import random

def getAnswer(answerNumber):
    if answerNumber ==1:
        return 'it is certain'
    elif answrNumber == 2:
        return 'It is decidedly so!'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Concentrate and ask again!'
    elif answerNumber == 6:
        return 'ask again later'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook is not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    print(getAnswer(random.randint(1,9)))
        
        
