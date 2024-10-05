def kbc_quiz():
    print("Welcome to Kaun Banega Crorepati! 🎉")
    
    # Define questions, options, and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. J.K. Rowling"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
            "answer": "B"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
            "answer": "B"
        }
    ]

    score = 0  # Initialize score

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Please enter your answer (A/B/C/D): ").upper()

        # Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct answer! 🎉")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {q['answer']}.")
    
    # Display the final score
    print(f"\nYour final score: {score}/{len(questions)}")
    if score==5:
       print("7.... crore....")
    print("Thank you for playing! 🎊")

if __name__ == "__main__":
    kbc_quiz()
