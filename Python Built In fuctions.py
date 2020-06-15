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


