import string
import random
from PyDictionary import PyDictionary

def getPasswordLen():
    length = int(input("How long do you want your password: "))
    return length

def useDigits():
    answer = input("Do you want to use digits? True or False")
    return answer.strip()

def useUpperLetters():
    answer = input("Do you want to use upper letters? True or False")
    return answer.strip()

def useLowerLetters():
    answer = input("Do you want to use lower letters? True or False")
    return answer.strip()

def usePunctuation():
    answer = input("Do you want to use punctuation? True or False")
    return answer.strip()

def repeatCharacters():
    answer = input("Do you allow to repeat characters? True or False")
    return answer.strip()

def generatePassword(choises_list, length):
    characters = []
    if choises_list[0] == 'True':
        characters = string.digits

    if choises_list[1] == 'True':
        characters += string.ascii_uppercase

    if choises_list[2] == 'True':
        characters += string.ascii_lowercase

    if choises_list[3] == 'True':
        characters += string.punctuation

    if choises_list[4] == 'True':
        str = ''.join(random.choices(characters, weights=None, cum_weights=None, k=length))
        return str

    elif choises_list[4] != 'True':
        str = ''.join(random.sample(characters,length))
        return str


def generateRandomPassword():
    length = getPasswordLen()
    list = []
    list.append(useDigits())
    list.append(useUpperLetters())
    list.append(useLowerLetters())
    list.append(usePunctuation())
    list.append(repeatCharacters())
    password = generatePassword(list, length)
    return password

def shuffleSentence():

    sentence = input("Please Enter Your Sentence to Be Shuffled: ")
    l1 = list(sentence)
    random.shuffle(l1)
    result = ''.join(l1)
    return result

def enterSentence():
    sentence = input("Please Enter Your Sentence For Creating Password: ")
    l1 = sentence.split(' ')
    random.shuffle(l1)
    result = ''
    for i in range(len(l1)):
        letter = l1[i][0]
        result += letter

    return result

def dictionaryMethod():

    dictionary = PyDictionary()
    sentence = input("Please Enter Random Word: ")
    meaning = dictionary.meaning(sentence)
    value = str(meaning.values())
    l1 = value.split(' ')
    num = int(input(" How Many Words Do You Want to Use? "))
    l2 = []
    for i in range(num):
        word = random.choice(l1)
        l2.append(word)
    random.shuffle(l2)
    result = ''
    for i in range(len(l2)):
        letter = l2[i][0]
        result += letter

    return result

if __name__ == '__main__':
    print("Welcome to Password Generator!!!")
    print ("Option 1:Generate Random Password \nOption 2 : Enter Sentence to Shuffle \n" +
           "Option 3: Enter Sentence For Creating Password \n "+
           "Option 4: Dictionary Method For Creating Password ")
    option = int(input(" Choose one of the options: "))
    password = ''
    if option == 1:
        password = generateRandomPassword()
    if option == 2:
        password = shuffleSentence()
    if option == 3:
        password = enterSentence()
    if option == 4:
        password = dictionaryMethod()
    print ("Your Password is : ",password)

