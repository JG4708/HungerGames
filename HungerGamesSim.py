import random


boys = ["Arnold", "Bobby", "Charles", "Connor", "Steve", "Xavier", "Gabriel", "Xenk", "Jack", "Jarnathan", "Peter", "Elias", "Miles", "Maximus", "John"]
girls = ["Kate",  "Alice", "Olivia", "Violet", "Rue", "Ruby", "Elizabeth", "Rita", "Shelly", "Vivian", "Sarah", "Emily", "Juliette", "Lucille",]
death = [" got stabbed and died.", " stepped on a land mine and died", " fell of a cliff", " was decapitated by a sword", " was attacked by tracker jackers", " died from hypothermia", " starved to death", " was shot through the heart with an arrow", " was betrayed by an ally and killed", " died from sever burns", " inhaled too much smoke", " was eaten by a bear"]
lives = [" made an alliance with another tribute", " built a fire" ]
goingToDie = []
goingToLive = []

tributeGirls = []
tributeBoys = []
tributes = []
day = 0

#USE f strings
#EXAMPLE:
#list1 = ["apple", "banana"]
#list2 = ["red", "yellow"]
# Pair 'apple' and 'red'
#combined = f"{list1[0]} {list2[0]}"


def chooseBoy():
    global boys, tributes, tributeBoys
    boy = random.choice(boys)
    if boy in tributeBoys:
        boys.remove(boy)
        boy = random.choice(boys)
    tributeBoys.append(boy)
    boys.remove(boy)
    return boy

def chooseGirl():
    global girls, tributes, tributeGirls
    girl = random.choice(girls)
    if girl in tributeGirls:
        boys.remove(girl)
        girl = random.choice(girl)
    tributeGirls.append(girl)
    girls.remove(girl)
    return girl


def runARound():
    global day, tributes,

num = int(input("How many tributes would you like to enter (max 24)? "))

for x in range(num):
    user = input("Is this tribute a boy or a girl? ")
    if user == "boy" or user == "Boy":
        userName = input("Name of tribute: ")
        tributeBoys.append(userName)
    elif user == "girl" or user == "Girl":
        userName = input("Name of tribute: ")
        tributeGirls.append(userName)
    else:
        print("'{}' is not an option, try again" .format(user))
        user = input("Is this tribute a boy or a girl? ")


while len(tributeBoys) < 12:
    chooseBoy()
while len(tributeGirls) < 12:
    chooseGirl()

for x in tributeBoys:
    tributes.append(x)
for x in tributeGirls:
    tributes.append(x)

print(tributes)



#while len(tributes) > 1: