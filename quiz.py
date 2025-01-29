questions = ("How many bones are in a cat’s body?", "What is the capital of Australia?", "Which planet is known as the “Red Planet”?", "In which year did the Titanic sink?", "What is the term for a group of crows?")

options =(("A. 206", "B. 230", "C. 195", "D. 250"), ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"), ("A. Venus", "B. Jupiter", "C. Mars", "D. Mercury"), ("A. 1912", "B. 1920", "C. 1908", "D. 1915"), ("A. Flock", "B. Murder", "C. Pack", "D. Swarm"))

answers = ("B", "C", "C", "A", "B")

guesses = []

score = 0
question_num = 0

for question in questions:
  print("------------------------------------")
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter (A, B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score+=1
    print("CORRECT!")
  else: 
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")
  question_num+=1

print("------------------------------------")
print("----------   RESULTS   -------------")
print("------------------------------------")

print("answers: ", end="")
for answer in answers: 
  print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses: 
  print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")