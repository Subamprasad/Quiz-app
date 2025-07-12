from .question_base import Question

class MCQQuestion(Question):
    """
    Multiple Choice Question subclass.
    """
    def __init__(self, prompt, options, answer, difficulty):
        super().__init__(prompt, answer, difficulty)
        self.options = options

    def ask(self):
        print(f"\n{self.prompt}")
        for idx, opt in enumerate(self.options, 1):
            print(f"  {idx}. {opt}")
        user_input = input("Your answer (number): ")
        return self.options[int(user_input)-1] if user_input.isdigit() and 1 <= int(user_input) <= len(self.options) else None 