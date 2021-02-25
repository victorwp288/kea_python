# Ex 1: Alphabet List Comprehensions

# Create a list of capital letters in the english alphabet

# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.

# Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

# Ex 2: Clothes List Comprehension
# Solution



# From 2 lists, using a list comprehension, create a list containing:

# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

# If the tuple pair is in the following list, it should not be added to the comprehension generated list.

soled_out = [('Black', 'm'), ('White', 's')]





# Ex 3: List & tuple exercises

# Based on these exercises from last time, solve the exercises by using list comprehensions instead.

# List & tuple exercises

# Modules

# Ex 4: Sys module exercise


# Create a commandline tool that checks if the required aguments are present when you run the program, and if not tells you what is missing to run the program.

# If you run python python script.py the program should print an error saying Usage: python script.py [-it]{--rm} where the [] means required and the {} means optional.

# Ex 5: OS Module exercise


""" 
os_exercise.py
Do the following task using the os module
 """

 
""" 
1. create a folder and name the folder 'os_exercises.'                                                  
2. In that folder create a file. Name the file 'exercise.py'                                                                            
3. get input from the console and write it to the file.                                                 
4. repeat step 2 and 3 (name the file something else).                                                  
5. read the content of the files and and print it to the console.
Ex 6: Extract .py files
"""

# Create a commandline utillity (program) that when run takes 1-3 commandline arguments where:

# * the first is the name of a directory in play
# * the second (optional) is a –flag (–todir <dirname>) that specifies where the files in that directory should be copied to.
# * the third (optional) is a –flag (–zip <filename>) that specifies if the files should be zipped and what the zip file should be called.
# So if you run the program like this python extract.py . --todir /tmp/ --zip archive.zip you should copy all files in the current directory (.) to a new tmp directory and the .py files should be put in a zip folder names archive.zip.

# Task A:
# Copy all .py files in a given directory to a new folder.

# Task B:
# Zip all .py files in a given directory and put the zip file in the specified folder.

# Ex 7: Simple scraber with requests
# Solution

# 1. Create an application that asks for an url.
# 2. Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page.
# 3. When done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).
# You will have to use the requests module, the OS module and the subprocesses module for this taks.