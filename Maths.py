# Trigonometry, ceiling, floor and constants

import math

print(math.pi)
print(math.e)

print(math.nan)
print(math.inf)

# Trigonometry
obstacle = math.cos(math.pi/4)
print(obstacle)
print(math.sin(math.pi/4))

# Ceiling and floor
cookies = 10.3
candy = 7
print(math.ceil(cookies))
print(math.ceil(candy))

age = 47.5
print(math.floor(age))


# Factorial, square root and GCD
print(math.factorial(3))
print(math.sqrt(64))

## GCD (Greatest common denominator)
print(math.gcd(52,8))
print(math.gcd(2, 13))

print(8/52)
print(2/13) # reduced faction of 8/52

# Degrees and Radians
print(math.radians(360))
print(math.pi*2)

print(math.degrees(math.pi*2))

# Python Random

import random
print(random.random())

decider = random.randrange(2)
if decider == 0:
    print("heads")
else:
    print("Tails")

print(decider)


print("You rolled a " + str(random.randrange(1,7)))

lottery_winners = random.sample(range(100), 5)
print(lottery_winners)

possible_pets = ["cat", "dog", "fish"]
print(random.choice(possible_pets))


possible_pets = ["cat", "dog", "fish"]
random.shuffle(possible_pets)
print(possible_pets)


# Statistics - Mean, mode, Standard Deviation
import statistics

agesData = [ 10, 14, 16, 18 , 91]

print(statistics.mean(agesData))
print(statistics.median(agesData))
print(statistics.mode(agesData))
print(sorted(agesData))

## Variance (average of squared differences from mean) and Standard Deviation 
print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))

#












