def get_questions():
    # Categorized questions by difficulty levels
    return {
        "Easy": [
            {"question": "What is the capital of Japan?", "answer": "Tokyo"},
            {"question": "How many planets are there in the solar system?", "answer": "8"},
            {"question": "What is the largest mammal?", "answer": "Blue whale"},
            {"question": "What is the primary ingredient in guacamole?", "answer": "Avocado"},
            {"question": "What is the chemical symbol for gold?", "answer": "Au"},
            {"question": "What is the tallest animal in the world?", "answer": "Giraffe"},
            {"question": "What is the main ingredient in a margarita cocktail?", "answer": "Tequila"},
        ],
        "Medium": [
            {"question": "What year did World War II end?", "answer": "1945"},
            {"question": "Who painted 'The Starry Night'?", "answer": "Vincent van Gogh"},
            {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria"},
            {"question": "What is the capital of Australia?", "answer": "Canberra"},
            {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
            {"question": "What is the largest organ in the human body?", "answer": "Skin"},
            {"question": "What is the world's largest desert?", "answer": "Antarctica"},
        ],
        "Hard": [
            {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
            {"question": "What is the tallest building in the world?", "answer": "Burj Khalifa"},
            {"question": "What is the boiling point of water in Fahrenheit?", "answer": "212°F"},
            {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
            {"question": "Who discovered the theory of relativity?", "answer": "Albert Einstein"},
            {"question": "What is the world's largest island?", "answer": "Greenland"},
            {"question": "What is the chemical formula for table salt?", "answer": "NaCl"},
        ],
    }
def ask_questions(questions, level, time_limit):
    score = 0
    for q in questions[level]:
        print(f"Time remaining: {time_limit} seconds")
        user_answer = input(q["question"] + " ")
        
        start_time = time.time()
        
        while time.time() - start_time < time_limit:
            # Check if the answer is provided within the time limit
            if user_answer.strip():
                break
        
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was {q['answer']}")
    return score
def main():
    all_questions = get_questions()
    levels = ["Easy", "Medium", "Hard"]
    total_score = 0
    time_limit_per_question = 20  # Set the time limit for each question (in seconds)

    for level in levels:
        print(f"Starting {level} level...")
        score = ask_questions(all_questions, level, time_limit_per_question)
        total_score += score
        print(f"Your score for {level} level is {score}")

    # Final score and message
    print(f"Final Score: {total_score}")

if __name__ == "__main__":
    main()
