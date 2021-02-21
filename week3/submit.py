directors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

# who in the board of directors is not an employee?
notEmployee = directors.difference(employees)
print(f"\nDirector, but not employee:\n{notEmployee}\n")

# who in the board of directors is also an employee?
alsoEmployee = directors.intersection(employees)
print(f"Director, and also employee:\n{alsoEmployee}\n")

# how many of the management is also member of the board?
numberOfMagenemt = management.intersection(directors)
howManyManagement = len(numberOfMagenemt)
print(f"Number of pepol in mangenemnt also in the board:\n{howManyManagement}\n")

# All members of the managent also an employee
managementAlsoEmployee = management.intersection(employees)
print(f"Management but also employee:\n{managementAlsoEmployee}\n")

# All members of the management also in the board?
managementAlsoBoard = management.intersection(directors)
print(f"Management but also director:\n{managementAlsoBoard}\n")

# Who is an employee, member of the management, and a member of the board?
holder = directors.intersection(management)
holder.intersection(employees)
print(f"People who is a member of management, employee and of the board:\n{holder}\n")

# Who of the employee is neither a memeber or the board or management?
onlyEmployees = (employees.difference(management))
onlyEmployees.difference(employees)
print(f"Employees with is neither a member of the board or mangement:\n{onlyEmployees}\n")



# 2. Using a list comprehension create a list of tuples from the folowing datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
myDict = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
myList = []

for i in myDict:
    k = (i, myDict[i])
    myList.append(k)

print(f"List of tuples:\n{myList}\n")


# 3. From these 2 sets:
# {'a', 'e', 'i', 'o', 'u', 'y'}
# {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

englishVowels = {'a', 'e', 'i', 'o', 'u', 'y'}
nordicVowels = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Union
englishUnionNordic = englishVowels.union(nordicVowels)
print(f"Union with nordic & english vowels:\n{englishUnionNordic}\n")

# Symmetric Difference
englishSymDifferenceNordic = englishVowels.symmetric_difference(nordicVowels)
print(f"Symmetric Difference with nordic & english vowels:\n{englishSymDifferenceNordic}\n")

# Difference
englishDifferenceNordic = englishVowels.difference(nordicVowels)
print(f"{englishDifferenceNordic}\n")

# disjoint
englishDisjointNordic = englishVowels.isdisjoint(nordicVowels)
print(f"{englishDisjointNordic}\n")


# 4. Date Decoder
monthDict = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12
}

def decoder (convertDate):
    convertedDateList = []
    date_split = convertDate.split('-')

    if int(date_split[2]) <= 10:
        year = '20' + date_split[2]
    else:
        year = '19' + date_split[2]

    convertedDateList.append(year)

    month = monthDict[date_split[1].upper()]
    convertedDateList.append(month)

    day = date_split[0]
    convertedDateList.append(day)

    return convertedDateList

userDate = input("Enter a date (format: dd-MMM-yy)\n>")
print(decoder(userDate))

    