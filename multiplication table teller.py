import pyttsx3

n = input("enter the number :")
dic = {
    "1": "ones",
    "2": "twos",
    "3": "threes",
    "4": "fours",
    "5": "fives",
    "6": "sixes",
    "7": "sevens",
    "8": "eights",
    "9": "nines",
    "10": "tens",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "ninteen",
    "20": "twenty"


}
txt = ""
for i in range(1, 11):
    mul = i*int(n)
    txt += str(i) + " " + dic[n] + " are " + str(mul) + "\n"
print(txt)

engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()