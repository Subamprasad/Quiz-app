import random
import json
from questions.question_factory import QuestionFactory
from core.score_manager import ScoreManager
from core.timer import Timer
from core.observer import QuizObserver

class QuizManager:
    def __init__(self, questions_file, num_questions=10, time_limit=60):
        self.questions_file = questions_file
        self.num_questions = num_questions
        self.time_limit = time_limit
        self.questions = []
        self.score_manager = ScoreManager()
        self.timer = Timer()
        self.time_up = False
        self.observer = QuizObserver(self.handle_time_up)
        self.timer.add_observer(self.observer)

    def load_questions(self):
        with open(self.questions_file, 'r', encoding='utf-8') as f:
            all_questions = json.load(f)
        # Sort by difficulty, then shuffle within each difficulty
        all_questions.sort(key=lambda q: q['difficulty'])
        self.questions = [QuestionFactory.create_question(q) for q in all_questions]

    def select_questions(self):
        # Select questions from easy to hard
        easy = [q for q in self.questions if q.difficulty == 'easy']
        medium = [q for q in self.questions if q.difficulty == 'medium']
        hard = [q for q in self.questions if q.difficulty == 'hard']
        selected = []
        selected += random.sample(easy, min(3, len(easy)))
        selected += random.sample(medium, min(4, len(medium)))
        selected += random.sample(hard, min(3, len(hard)))
        random.shuffle(selected)
        return selected[:self.num_questions]

    def handle_time_up(self):
        print("\nTime is up!")
        self.time_up = True

    def run_quiz(self):
        self.load_questions()
        questions = self.select_questions()
        self.score_manager.reset()
        self.time_up = False
        print(f"\nStarting quiz: {self.num_questions} questions, {self.time_limit} seconds total.")
        self.timer.start(self.time_limit)
        for idx, q in enumerate(questions, 1):
            if self.time_up:
                break
            print(f"\nQuestion {idx}:")
            user_answer = q.ask()
            if self.time_up:
                break
            if q.check_answer(user_answer):
                print("Correct!")
                self.score_manager.add(1)
            else:
                print(f"Incorrect. Correct answer: {q.answer}")
        self.timer.stop()
        print(f"\nQuiz finished! Your score: {self.score_manager.get_score()} / {len(questions)}") 