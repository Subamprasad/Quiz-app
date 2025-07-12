from .mcq import MCQQuestion
from .true_false import TrueFalseQuestion
from .fill_blank import FillBlankQuestion

class QuestionFactory:
    """
    Factory for creating question objects based on type.
    """
    @staticmethod
    def create_question(qdata):
        qtype = qdata.get('type')
        if qtype == 'mcq':
            return MCQQuestion(qdata['prompt'], qdata['options'], qdata['answer'], qdata['difficulty'])
        elif qtype == 'true_false':
            return TrueFalseQuestion(qdata['prompt'], qdata['answer'], qdata['difficulty'])
        elif qtype == 'fill_blank':
            return FillBlankQuestion(qdata['prompt'], qdata['answer'], qdata['difficulty'])
        else:
            raise ValueError(f"Unknown question type: {qtype}") 