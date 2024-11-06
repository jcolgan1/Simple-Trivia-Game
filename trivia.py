import requests
import json


inp1 = input("Welcome to Trivia! How many questions would you like? (1-50): ")
while (not (inp1.isdigit())) or int(inp1) < 1 or int(inp1) > 50:
    inp1 = input("Please enter an integer value (1-50): ")

url = f"https://opentdb.com/api.php?amount={inp1}&category=9&difficulty=medium&type=boolean"

response = requests.get(url)
if response.status_code != 200:
    print("Response Unsuccessful. Try again") 
else:
    data = response.json()
    
    with open('trivia.json', 'w') as file:
        json.dump(data, file, indent=4)  


#Next Step: Go through trivia questions