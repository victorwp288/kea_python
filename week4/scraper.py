
# 1. Create an application that asks for an url.
# 2. Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page.
# 3. When done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).
# You will have to use the requests module, the OS module and the subprocesses module for this taks.

import requests

url = requests.get('https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)')

if url:
    print('Success!')
else:
    print('An error has occurred.')


