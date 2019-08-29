import json 
import subprocess
import requests

api_url = "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25"

r = requests.get(api_url)	
data = r.json()

title = data["title"]
template = data["value"]
blanks = data["blanks"]

def ascii_art(phrase):
	subprocess.call("figlet " + phrase, shell=True)

ascii_art(title)



user_inputs = []
get_user_inputs()

def get_user_inputs():
	for blank in blanks:
		user_input = input("Enter " + blank + ": ")
		user_inputs.append(user_input)


fill_in_blanks()

def fill_in_blanks():
	counter = 1
	for i in range(len(user_inputs)):
		template.insert(i + counter ,user_inputs[i])
		counter += 1 




print(template)

