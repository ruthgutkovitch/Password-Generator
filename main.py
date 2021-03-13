import string
import random

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


if __name__ == '__main__':
    print("Welcome to Password Generator!!!")
    length = getPasswordLen()
    list = []
    list.append(useDigits())
    list.append(useUpperLetters())
    list.append(useLowerLetters())
    list.append(usePunctuation())
    list.append(repeatCharacters())
    password = generatePassword(list, length)
    print (password)

