from capitals import states
import random

#Test to access dictionary
print(states[3]['name'])
#print(states)

#Welcome Message:
welcome = input('Welcome to the game Guesstimation! PRESS ENTER key to start:')

# Random Shuffle content in states dictionaries
random.shuffle(states)

#Loop thru states array of dictionaries to be able to print out indexed state
for index in range(len(states)):
    for key in states[index]:
        capital_guess = input('Where is capital of ' + states[index][key] + ':')







