# First we will explore python's built in match functions

# Standard libraries - built in functions & built in imported modules
# Boolean

isRaining = True
isSunny = False

# logical operator - AND, OR, NOT
if isRaining and isSunny:
    print("you might see a rainbow")

if isRaining or isSunny:
    print("It might be rainy or sunny")

if not isSunny:
    print("It is Rainy")

# Example:
ages = [12,18, 39, 7, 2]

for age in ages:
    isAdult = age > 17;
    if  not isAdult:
        print("Being " + str(age) + " does not make you adult")



# Comparision Operators
## Greater than, equal to , less than
print(10 < 75)

if 10 < 75:
    print("This is bigger")

kitten = 10
tiger = 76
if kitten < tiger:
    print("Tiger is bigger")

mouse = 1
if mouse < kitten and mouse < tiger:
    print("mouse is smaller")


# calculating length:
firstName = "Taylor"
print(len(firstName))

firstName.__len__()

ages = [0,11,43]
print(len(ages))

i=0
for i in range(0, len(ages)):
    print(ages[i])

candyCollection = {"bob": 10, "mary": 15}
print(len(candyCollection))


# Range function:
numberedContestants = range(30)
print(len(numberedContestants))
for c in list(numberedContestants):
    print("Contestant " + str(c) + " is here") 

luckyWinners = range(7,30,5)
print(list(luckyWinners))

# Minimum and Maximum values
playerOneScore = 10
playerTwoScore = 20
print(min(playerOneScore, playerTwoScore))
print(min(-1, 5, -10))













