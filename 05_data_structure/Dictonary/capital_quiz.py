import random

capitals = {
    "USA": "Washington, D.C.",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "South Africa": "Pretoria"
}



import random

capitals = {
    "USA": "Washington, D.C.",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "South Africa": "Pretoria"
}

correct = 0
incorrect = 0

print("======Capital Quiz App======")
print("Type 'quit' to exit the game.\n")

while True:
    # Pick a random country
    random_key = random.choice(list(capitals.keys()))
    
    # Ask the user
    user_answer = input(f"Enter the capital of {random_key}: ")
    
    # Check if they want to quit
    if user_answer.lower() == 'quit':
        break
    
    # Check the answer (case-insensitive so "paris" matches "Paris")
    if user_answer.lower() == capitals[random_key].lower():
        correct += 1
        print(" Correct!")
    else:
        incorrect += 1
        print(f" Incorrect. The capital is {capitals[random_key]}.")
    
    # Show current score after each question
    print(f"Score: Correct = {correct} | Incorrect = {incorrect}\n")

# Final goodbye message
print(f"\nGame Over! Final Score -> Correct: {correct}, Incorrect: {incorrect}")