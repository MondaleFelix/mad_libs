import json 
import subprocess
import requests

api_url = "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25"

r = requests.get(api_url)	
data = r.json()

# JSON Object 
title = data["title"]
template = data["value"][:-1]
blanks = data["blanks"]
user_inputs = []

# Creates ascii art 
def ascii_art(phrase):
	subprocess.call("figlet " + phrase, shell=True)

# Gets user input for every blank.
def get_user_inputs():
	for blank in blanks:
		user_input = input("Enter " + blank + ": ")
		user_inputs.append(user_input)

# Fills in template with the collected user inputs
def fill_in_blanks():
	counter = 1
	for i in range(len(user_inputs)):
		template.insert(i + counter ,user_inputs[i])
		counter += 1 

def print_story():
	ascii_art(title)
	print(" ")
	print("".join(template))
	print(" ")


ascii_art("Mad Libs")
get_user_inputs()
fill_in_blanks()
print_story()
