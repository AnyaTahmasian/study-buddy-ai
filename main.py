import ollama
import random

def get_tutor_feedback(category, question, student_answer):
    # AI instruction
    system_prompt = (
        f"You are a knowledgeable Computer Science professor. "
        f"The student is studying {category}. "
        f"You asked: '{question}' "
        f"The student answered: '{student_answer}'."
    )
    
    # how AI behave
    user_instruction = (
        "Check if the answer is correct. If it is, say 'Correct!' and explain why. "
        "If it's wrong or incomplete, provide a clear, simple explanation to help them learn."
    )

    # Calling Ollama 
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_instruction},
    ])

    return response['message']['content']

# study topics
study_materials = {
    "Data Structures": [
        "What is the time complexity of searching in a Hash Table?",
        "Explain the difference between a Tree and a Graph."
    ],
    "Operating Systems": [
        "What is a deadlock and how can it be prevented?",
        "Describe the difference between a process and a thread."
    ],
    "Discrete Math": [
        "What is the Pigeonhole Principle?",
        "Explain the difference between a permutation and a combination."
    ]
}

# Randomly select a category and a question
category = random.choice(list(study_materials.keys()))
question = random.choice(study_materials[category])

print(f"--- Topic: {category} ---")
print(f"Question: {question}")

# Get the user's input
user_answer = input("Your Answer: ")

# Call the function and get the AI's response
print("\n--- Tutor Feedback ---")
feedback = get_tutor_feedback(category, question, user_answer)
print(feedback)


def main():
    print("Welcome to your CS Study Buddy!")
    print("Type 'quit' at any time to exit.\n")

    while True:
        # Step 4a: Let the user choose to continue or exit
        choice = input("Ready for a question? (press Enter to continue, or type 'quit'): ").lower()
        
        if choice == 'quit':
            print("Great job studying today! See you next time.")
            break
            
        # Step 4b: Run the quiz logic (from our previous steps)
        category = random.choice(list(study_materials.keys()))
        question = random.choice(study_materials[category])
        
        print(f"\n--- Topic: {category} ---")
        user_answer = input(f"Question: {question}\nYour Answer: ")
        
        if user_answer.lower() == 'quit':
            break

        # Step 4c: Get AI feedback
        print("\nThinking...")
        feedback = get_tutor_feedback(category, question, user_answer)
        print(f"Feedback: {feedback}\n")
        print("-" * 30)

# This actually starts the program
if __name__ == "__main__":
    main()