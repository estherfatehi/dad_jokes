import requests
import time

"""
This is a script that calls the https://icanhazdadjoke.com/api endpoint for a new set of jokes. 
The script accepts user input that would allow for a search term and the number of jokes in a set 
(example: I want to call 3 jokes with the search term 'snow'). 
The script accepts the response and provides each joke in the set individually, with a pause between each joke of 5 seconds.
"""

while True:
    search_term = input("Enter a search term to search the dad jokes database: ")
    if not search_term.isalpha():
        print("Search term must only contain letters")
    else:
        break

while True:
    num_jokes = input("Enter number of jokes you want printed: ")
    if not num_jokes.isnumeric():
        print("Number of jokes must be a number. Please try again")
    else:
        break

res = requests.get("https://icanhazdadjoke.com/search?limit={0}&term={1}".format(num_jokes, search_term), headers={"Accept":"text/plain"})
if res.status_code == 404:
        print("There are no jokes with your search term ...... yet")

joke_counter = 1
for line in res.text.splitlines():
    print("Joke {0}: ".format(joke_counter) + line)
    joke_counter += 1
    time.sleep(5)
