# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
#
# for i in range(6):
#     for a in range(9):
#         if a < 8:
#             print(grid[a][i], end="")
#         else:
#             print(grid[a][i])

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')

# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.findall('My number is 415-555-4242. 123-456-798, 444-553-4421')
# print(mo)

"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox"."""
import random, sys


def getBirthdays(numberOfBirthdays):
    """Returns a list of birthday dates."""
    birthdays = []
    for i in range(numberOfBirthdays):
        dayOfYear = random.randint(1, 365)
        if dayOfYear > 334:
            month = 'Dec'
            day = dayOfYear - 334
        elif dayOfYear > 304:
            month = 'Nov'
            day = dayOfYear - 304
        elif dayOfYear > 273:
            month = 'Oct'
            day = dayOfYear - 273
        elif dayOfYear > 243:
            month = 'Sep'
            day = dayOfYear - 243
        elif dayOfYear > 212:
            month = 'Aug'
            day = dayOfYear - 212
        elif dayOfYear > 181:
            month = 'Jul'
            day = dayOfYear - 181
        elif dayOfYear > 151:
            month = 'Jun'
            day = dayOfYear - 151
        elif dayOfYear > 120:
            month = 'May'
            day = dayOfYear - 120
        elif dayOfYear > 90:
            month = 'Apr'
            day = dayOfYear - 90
        elif dayOfYear > 59:
            month = 'Mar'
            day = dayOfYear - 59
        elif dayOfYear > 31:
            month = 'Feb'
            day = dayOfYear - 31
        elif dayOfYear > 0:
            month = 'Jan'
            day = dayOfYear - 0

        birthdays.append(month + str(day))
    return birthdays


def getMatch(birthdays):
    """Returns the birthday that occurs more than once in the list."""

    # Compare each birthday to every other birthday:
    for a in range(0, len(birthdays)):
        for b in range(a + 1, len(birthdays)):
            if birthdays[a] == birthdays[b]:
                return birthdays[a]  # Return the matching birthday.


# Display the intro:
print('Birthday Paradox (barebones version)')
print('by Al Sweigart al@inventwithpython.com')
print()
print('How many birthdays shall I generate? (Max 100)')
response = input('> ')
if not (0 < int(response) <= 100):
    print('That is larger than 100.')
    sys.exit()

numBDays = int(response)

# Generate and display the birthdays:
print()
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
print(', '.join(birthdays))
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this one simulation, ', end='')
if match != None:
    print('multiple people have a birthday on', match)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Running 100,000 simulations. Please wait...')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100000):
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('Done.')

# Display simulation results:
probability = round(simMatch / 1000, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That is probably more than you would think!')