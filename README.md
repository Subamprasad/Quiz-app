# IQ & GK Quiz App

## Overview
This is a command-line Quiz Application built in Python that tests users with a set of 10 IQ and General Knowledge questions. The app demonstrates the integration of multiple design patterns (Factory, Singleton, Observer) in a real-world mini-application.

## Features
- 10-question quiz session (from a pool of 100+ possible questions)
- Questions of increasing difficulty (easy, medium, hard)
- Multiple question types: MCQ, True/False, Fill-in-the-blank
- 1-minute timer for the whole quiz
- Scoring system and result summary
- Option to restart or exit after each quiz
- Clean, modular code using design patterns

## File Structure
```
quiz_app/
│
├── main.py                  # CLI entry point
├── README.md                # Project documentation
├── questions/
│   ├── question_base.py     # Base class for all questions
│   ├── question_factory.py  # Factory for creating questions
│   ├── mcq.py               # MCQ question class
│   ├── true_false.py        # True/False question class
│   └── fill_blank.py        # Fill-in-the-blank question class
│
├── core/
│   ├── quiz_manager.py      # Controls quiz flow
│   ├── score_manager.py     # Singleton for score tracking
│   ├── timer.py             # Singleton for quiz timer
│   └── observer.py          # Observer pattern for time-up events
│
├── data/
│   └── questions.json       # Question bank (edit to add more questions)
```

## How It Works
1. **Start the App**: Run `python main.py` from inside the `quiz_app` folder.
2. **Menu**: The app displays a welcome message and menu. Choose to start the quiz or exit.
3. **Quiz Session**:
   - 10 questions are selected (mix of easy, medium, hard, and types).
   - You have 1 minute to answer all questions.
   - Each question is shown one by one. Answer by typing your response.
   - The timer runs in the background. If time is up, the quiz ends immediately.
4. **Scoring**: After the quiz, your score out of 10 is displayed.
5. **Restart/Exit**: You can return to the menu to play again or exit.

## Design Patterns Used
- **Factory Pattern**: `question_factory.py` creates question objects (MCQ, True/False, Fill-in-the-blank) based on data.
- **Singleton Pattern**: `score_manager.py` and `timer.py` ensure only one instance manages score and timing.
- **Observer Pattern**: `observer.py` and `timer.py` notify the quiz manager when time is up.

## Logic Flow
- `main.py` handles the CLI and menu.
- When a quiz starts, `QuizManager` loads questions from `questions.json`, selects a balanced set, and starts the timer.
- For each question, the user is prompted for an answer. The answer is checked, and the score is updated.
- If the timer expires, the Observer notifies the quiz to end.
- After all questions or time up, the score is shown and the user can restart or exit.

## Customization
- Add more questions by editing `data/questions.json`.
- Adjust the number of questions or time limit in `main.py` or `quiz_manager.py`.

## Requirements
- Python 3.7 or higher

## Running the App
```
cd quiz_app
python main.py
```

---

Enjoy your quiz and feel free to expand the app with more features or a GUI! 