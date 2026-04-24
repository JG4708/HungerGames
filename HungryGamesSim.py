import random

boys = ["Arnold", "Bobby", "Charles", "Connor", "Steve", "Xavier", "Gabriel", "Xenk", "Jack", "Jarnathan", "Peter", "Elias", "Miles", "Maximus", "John"]
girls = ["Kate",  "Alice", "Olivia", "Violet", "Rue", "Ruby", "Elizabeth", "Rita", "Shelly", "Vivian", "Sarah", "Emily", "Juliette", "Lucille",]
goingToDie = []
outcomes = []
goingToLive = []
tributeGirls = []
tributeBoys = []
tributes = []
day = 0
go = "yes"


print()
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





def runRound():
    global day, tributes, outcomes, goingToDie, lives, death, goingToLive
    death = ["got stabbed and died.", "stepped on a land mine and died", "fell of a cliff",
             "was decapitated by a sword", "was attacked by tracker jackers and died", "died from hypothermia",
             "starved to death", "was shot through the heart with an arrow", "was betrayed by an ally and killed",
             "died from sever burns", "inhaled too much smoke and died", "was eaten by a bear",
             "was poisoned by another tribute", "lost a one-on-one duel to the death", "drowned in a lake",
             "was caught in a forest fire", "fell out of a tree and died", "ate a poisonous berry",]
    lives = ["made an alliance with another tribute", "built a fire", "slept the whole day", "eats a lot of food",
             "received a gift from sponsors", "practiced with their weapons", "tames a rabbit",
             "breaks an alliance", "bonds with another tribute while singing Golden", "thinks of home",
             "hunts for food", "sets up camp", "enjoys the sunrise", "kills a bear", "climbed a tree", "stalked another tribute",
             "surveyed the arena", "had a mental breakdown", "ran around delirious", "performed a rain dance", "performed a satanic ritual"]
    day += 1
    goingToDie = []
    goingToLive = []
    print()
    print("DAY {}".format(day))
    print()
    numDie = random.randint(0, len(tributes)-1)
    

    # HOW MANY DIE
    for x in range(numDie):
        random.shuffle(tributes)
        goingToDie.append(tributes[0])
        tributes.remove(tributes[0])


    # DEAD
    for x in range(len(goingToDie)):
        storyline = f"{goingToDie[0]} {death[0]}"
        goingToDie.remove(goingToDie[0])
        random.shuffle(death)
        outcomes.append(storyline)


    #LIVING
    for x in tributes:
        goingToLive.append(x)
        storyline = f"{goingToLive[0]} {lives[0]}"
        random.shuffle(lives)
        outcomes.append(storyline)
        goingToLive.remove(x)




    for x in range(len(outcomes)):
        random.shuffle(outcomes)
        print(outcomes[0])
        outcomes.remove(outcomes[0])


    print()
    print("There are {} tributes left.".format(len(tributes)))





print("""Welcome to the Hunger Games!""")
print("""╔╦╗┌─┐┬ ┬  ╔╦╗┬ ┬┌─┐  ╔═╗┌┬┐┌┬┐┌─┐  ╔╗ ┌─┐
║║║├─┤└┬┘   ║ ├─┤├┤   ║ ║ ││ ││└─┐  ╠╩╗├┤ 
╩ ╩┴ ┴ ┴    ╩ ┴ ┴└─┘  ╚═╝─┴┘─┴┘└─┘  ╚═╝└─┘""")
print("""███████╗██╗   ██╗███████╗██████╗     ██╗███╗   ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███████╗ █████╗ ██╗   ██╗ ██████╗ ██████╗ 
██╔════╝██║   ██║██╔════╝██╔══██╗    ██║████╗  ██║    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔═══██╗██╔══██╗
█████╗  ██║   ██║█████╗  ██████╔╝    ██║██╔██╗ ██║     ╚████╔╝ ██║   ██║██║   ██║██████╔╝    █████╗  ███████║██║   ██║██║   ██║██████╔╝
██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║██║╚██╗██║      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██╔══╝  ██╔══██║╚██╗ ██╔╝██║   ██║██╔══██╗
███████╗ ╚████╔╝ ███████╗██║  ██║    ██║██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝██║  ██║    ██║     ██║  ██║ ╚████╔╝ ╚██████╔╝██║  ██║
╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                       """)
print()

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


while len(tributes) > 1 and (go == "Yes" or go == "yes"):
        print()
        runRound()
        print()
        go = input("Say yes when ready for next round: ")
        print("Next day...")






if len(tributes) == 1:
    for x in tributes:
        print("{} is the winner of the hunger games!".format(x))

