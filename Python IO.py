
# Command line arguments
import sys
sys.argv
print(len(sys.argv))

print("Number of arguments:", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv)

# Remove arguments
# sys.argv.remove(sys.argv[0])

# Setting up argument
arguments = sys.argv
sum = 2
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad Input")

print(sum)


# input and output
## Output
print("Hello")
## Input
# color = input("what is your favourite color")
# print(color)

# Files and File Writing

# Open a file
myFile = open("scores.txt", "w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
print("Reading..." + myFile.read(10)) # read only 10 characters
myFile.seek(0) # Setting a seek point
print("Reading again" + myFile.read(10))

#

