import requests
import json


inp1 = input("Welcome to Trivia! How many questions would you like? (1-50): ")
while (not (inp1.isdigit())) or int(inp1) < 1 or int(inp1) > 50:
    inp1 = input("Please enter an integer value (1-50): ")


while True:
    inp2 = input("Please enter Easy, Medium, or Hard: ")
    if inp2.lower() == "medium" or inp2.lower() == "hard" or inp2.lower() == "easy":
        break

url = f"https://opentdb.com/api.php?amount={inp1}&category=9&difficulty={inp2.lower()}&type=boolean"

response = requests.get(url)
if response.status_code != 200:
    print("Response Unsuccessful. Try again") 
else:
    data = response.json()
    
    with open('trivia.json', 'w') as file:
        json.dump(data, file, indent=4)  


#Next Step: Go through trivia questions

# Load trivia questions from the file
with open('trivia.json', 'r') as file:
    trivia_data = json.load(file)

questions = trivia_data.get('results', [])

if not questions:
    print("No questions found in the file. Exiting...")
    exit()

score = 0

# Loop through each question and ask the user
for i, question in enumerate(questions, start=1):
    print(f"Question {i}: {question['question']}")
    user_answer = input("Your answer (True/False): ").strip().capitalize()

    # Validate user input
    while user_answer not in ["True", "False"]:
        user_answer = input("Please answer 'True' or 'False': ").strip().capitalize()

    # Check if the answer is correct
    correct_answer = question['correct_answer']
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")

# Display the final score
print(f"You got {score} out of {len(questions)} questions correct!")