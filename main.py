from  datetime import datetime
import os

alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
reverseCouple = [["a","z"], ["b","y"], ["c","x"], ["d","w"], ["e","v"], ["f","u"], ["g","t"], ["h","s"], ["i","r"], ["j","q"], ["k","p"], ["l","o"], ["m","n"], ["n","m"], ["o","l"], ["p","k"], ["q","j"], ["r","i"], ["s","h"], ["t","g"], ["u","f"], ["v","e"], ["w","d"], ["x","c"], ["y","b"], ["z","a"]]


def captureDate(): 
    now = datetime.now()
    f_date = now.strftime("%H%M%S")
    return f_date    #used as a shift

def cypherStrength():
    s = int(input("Enter cypher strengh:\n[ 1 | 2 | 3 ]"))
    if s == 1 or s == 2 or s == 3:
        return s
    else:
        print("Invalid Strenght...")
        os.system('cls')
        cypherStrength()


def encode(message, key = ""):
    cypher = ""
    #strength = cypherStrength()
    if key == "":
        #encode without a key

        #Substituting each character for their couple in the reverse couple
        for letter in message:
            for couple in reverseCouple:
                if letter == couple[0]:
                    cypher += couple[1]

        #The time is retrieved in the format 123456

        print(cypher)

    if len(key) > 0:
        #encode with key
        pass

def decode(message, key = ""):
    if key == "":
        #decode without a key
        pass

    if len(key) > 0:
        #decode with key
        pass
    pass

encode("hello my name is daniel")