import os
from core.quiz_manager import QuizManager

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    questions_file = os.path.join(os.path.dirname(__file__), 'data', 'questions.json')
    while True:
        clear_screen()
        print("=== Welcome to the IQ & GK Quiz App ===")
        print("1 minute quiz and have a 10 question all the best")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            quiz = QuizManager(questions_file, num_questions=10, time_limit=60)
            quiz.run_quiz()
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main() 