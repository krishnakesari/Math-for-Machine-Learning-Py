
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


