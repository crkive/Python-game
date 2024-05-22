import random

# Function to display a question
def displayQuestion(question, options, questionNumber, currentReward):
    print(f"\nQuestion {questionNumber}: {question}")
    # Display each option with a number
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    print(f"Current reward: ${currentReward}")

# Function to implement the lifeline "50/50"
def fiftyFifty(options, correctAnswer):
    # Randomly choose one incorrect option
    incorrectOption = random.choice(options)
    # Ensure that the incorrect option chosen is not the correct answer
    while incorrectOption == correctAnswer:
        incorrectOption = random.choice(options)
    # Create the list with the correct and incorrect options
    fiftyFiftyOption = [correctAnswer, incorrectOption]
    return fiftyFiftyOption

def main():
    # List of questions, each question represented as a list containing the question, options, and correct answer
    questions = [
        ["What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Berlin"], "B. Paris"],
        ["What is the largest planet in our solar system?", ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"], "B. Jupiter"],
        ["Who wrote 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"], "A. William Shakespeare"],
        ["Which is the longest river in the world?", ["A. Nile", "B. Amazon", "C. Mississippi", "D. Yangtze"], "A. Nile"],
        ["What is the chemical symbol for water?", ["A. H2O", "B. CO2", "C. O2", "D. NaCl"], "A. H2O"],
        ## add more questions here 
    ]
    # Number of remaining lifelines
    lifelinesRemaining = 2
    # Current reward earned by the player
    currentReward = 0
    # Number of the current question
    questionNumber = 1

    print("Welcome to Who Wants to Be a Millionaire!\n")

    # Loop through each question
    while questionNumber <= len(questions):
        # Get the current question data
        question, options, correctAnswer = questions[questionNumber - 1]
        # Display the question and options
        displayQuestion(question, options, questionNumber, currentReward)
        # Check if lifelines are available
        if lifelinesRemaining:
            # Ask the player if they want to use a lifeline
            lifeline_input = input("Would you like to use a lifeline? (Type 'y' to use): ")
            if lifeline_input == 'y':
                # Use the "50/50" lifeline and display the reduced options
                fiftyFiftyOption = fiftyFifty(options, correctAnswer)
                print(f"The options reduced to {fiftyFiftyOption}")
                # Decrement the number of remaining lifelines
                lifelinesRemaining -= 1

        # Get the player's answer
        answer = input("Your answer: ")
            # Check if the answer is correct
        if answer == correctAnswer.split('.')[0]:
            # Increment the reward if the answer is correct
            currentReward += 100
            print("Correct!\n")
         
        else:
            # Print the correct answer if the answer is incorrect
            print(f"Incorrect! The correct answer is: {correctAnswer}")
            # End the game loop if the answer is incorrect
            break

        # Move to the next question
        questionNumber += 1

    # Print the final result
    print(f"\nGame over! You won ${currentReward}")

if __name__ == "__main__":
    main()
