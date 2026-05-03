import random
import math
import os
import sys
import turtle
# Quiz Questions
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A) Delhi", "B) Mumbai", "C) Chennai", "D) Kolkata"],
        "answer": "A"
    },
    {
        "question": "2. Which language is used for Python?",
        "options": ["A) HTML", "B) Java", "C) Programming", "D) CSS"],
        "answer": "C"
    },
    {
        "question": "3. What is 5 + 3 ?",
        "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
        "answer": "B"
    },
    {
        "question": "4. Which planet is called Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "5. Who invented Python?",
        "options": ["A) Guido van Rossum", "B) Elon Musk", "C) Bill Gates", "D) Steve Jobs"],
        "answer": "A"
    }
    {
        "question": "6. Who is known as Father of Computers?",
        "options": ["A) Charles Babbage", "B) Newton", "C) Einstein", "D) Tesla"],
        "answer": "A"
    },
    {
        "question": "7. Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question": "8. Which data type is used to store text in Python?",
        "options": ["A) int", "B) float", "C) str", "D) bool"],
        "answer": "C"
    },
    {
        "question": "9. What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Computer Unit", "C) Control Unit", "D) Central Unit"],
        "answer": "A"
    },
    {
        "question": "10. Which symbol is used for comments in Python?",
        "options": ["A) //", "B) /* */", "C) #", "D) --"],
        "answer": "C"
    },
    {
        "question": "11. Which company developed Python?",
        "options": ["A) Microsoft", "B) Google", "C) Python Software Foundation", "D) IBM"],
        "answer": "C"
    },
    {
        "question": "12. Which function is used to take input in Python?",
        "options": ["A) scan()", "B) input()", "C) read()", "D) get()"],
        "answer": "B"
    },
    {
        "question": "13. Which keyword is used for loop in Python?",
        "options": ["A) loop", "B) iterate", "C) for", "D) repeat"],
        "answer": "C"
    },
    {
        "question": "14. Which data type is used for True/False?",
        "options": ["A) int", "B) str", "C) bool", "D) float"],
        "answer": "C"
    },
    {
        "question": "15. Which keyword is used for condition in Python?",
        "options": ["A) check", "B) if", "C) condition", "D) when"],
        "answer": "B"
    },
    {
        "question": "16. Which function prints output in Python?",
        "options": ["A) display()", "B) print()", "C) show()", "D) output()"],
        "answer": "B"
    },
    {
        "question": "17. Which symbol is used for power in Python?",
        "options": ["A) ^", "B) **", "C) //", "D) %"],
        "answer": "B"
    }
    ]
# Random package functionality
random.shuffle(questions)

score = 0
total = len(questions)
# Quiz Start
print("================================")
print("      WELCOME TO QUIZ GAME      ")
print("================================")

for q in questions:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
# Math package functionality
percentage = math.ceil((score / total) * 100)
# Result Section
print("\n================================")
print("          FINAL RESULT          ")
print("================================")
print("Score:", score, "/", total)
print("Percentage:", percentage, "%")

if percentage >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
# Turtle package functionality
screen = turtle.Screen()
screen.title("Quiz Result")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-150, 0)

pen.write("Congratulations!\nQuiz Completed",
          font=("Arial", 18, "bold"))
# Exit using sys package
choice = input("\nEnter Q to Quit: ").upper()

if choice == "Q":
    print("Thank You!")
    sys.exit()

turtle.done()