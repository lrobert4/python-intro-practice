from capitals import states
import random

#Test to access dictionary
print(states[3]['name'])
#print(states)

#Welcome Message:
welcome = input('Welcome to the game Guesstimation! PRESS ENTER key to start:')

# Random Shuffle content in states dictionaries
random.shuffle(states)

# Add Keys in dictionaries to store number of times right or wrong
#count = 0
#for count in range(len(states)):
    #states["ricount"]= 0
    #states["wrcount"]= 0

#Loop thru states array of dictionaries to be able to print out indexed state
for index in range(len(states)):
    for key in states[index]:
        capital_guess = input('Where is capital of ' + states[index][key] + ':')







