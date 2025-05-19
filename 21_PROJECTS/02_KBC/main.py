# List of questions, options, and correct answers (last element in each sublist is the correct option index)
questions = [
    ["Who is Shahrukh Khan?", "WWE Wrestler", "Actor", "Cricketer", "Musician", 2],
    ["What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", 2],
    ["What is the square root of 64?", "6", "7", "8", "9", 3],
    ["Which is the smallest continent?", "Africa", "Australia", "Europe", "South America", 2],
    ["What is the boiling point of water in Celsius?", "90", "100", "110", "120", 2],
    ["Who discovered gravity?", "Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which language is used to write Android apps?", "Python", "Java", "C++", "Ruby", 2]
]

# List of prizes corresponding to each question
prizes  = [1000,10000,20000,40000,80000,160000,320000,640000,1280000,2500000]

# Initialize question index
i = 0

# Loop through each question
for question in questions:
    # Display the question and options
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Get the user's answer
    a = int(input("Enter your answer: \n[1 for a, 2 for b, 3 for c, 4 for d]\n1"))
    
    # Check if the answer is correct
    if(question[5] == a):
        print("Correct Answer")
    else:
        # If incorrect, display the correct answer and exit the game
        print(f"Incorrect answer!, The correct answer is {question[5]}")
        print("Better Luck! Try Next Time.")
        break
    
    # Display the prize won for the current question
    print(f"You won {prizes[i]}")
    i += 1  # Move to the next question