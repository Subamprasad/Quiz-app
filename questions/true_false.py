from .question_base import Question

class TrueFalseQuestion(Question):
    """
    True/False Question subclass.
    """
    def __init__(self, prompt, answer, difficulty):
        super().__init__(prompt, answer, difficulty)

    def ask(self):
        print(f"\n{self.prompt} (True/False)")
        user_input = input("Your answer: ")
        return user_input.strip().capitalize() 