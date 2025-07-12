class Question:
    """
    Abstract base class for all question types.
    """
    def __init__(self, prompt, answer, difficulty):
        self.prompt = prompt
        self.answer = answer
        self.difficulty = difficulty

    def ask(self):
        """Display the question and return user's answer."""
        raise NotImplementedError

    def check_answer(self, user_answer):
        """Check if the user's answer is correct."""
        return user_answer.strip().lower() == str(self.answer).strip().lower() 