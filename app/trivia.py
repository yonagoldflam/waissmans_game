from __future__ import annotations

from pydantic import BaseModel


class TriviaQuestion(BaseModel):
    id: str
    question: str
    answers: list[str]
    correct_answer: int
    explanation: str


# כל החידון נמצא בקובץ זה. הוסיפו שאלות למערך באותו מבנה.
TRIVIA_QUESTIONS = [
    TriviaQuestion(
        id="burial-pairs",
        question="אילו זוגות קבורים במערת המכפלה על פי המסורת המובאת בחוברת?",
        answers=[
            "אברהם ושרה, יצחק ורבקה, יעקב ולאה",
            "משה וציפורה, אהרן ואלישבע",
            "דוד ובת שבע, שלמה ונעמה",
        ],
        correct_answer=0,
        explanation="נכון! בחוברת נזכרים שלושת זוגות האבות והאימהות: אברהם ושרה, יצחק ורבקה, יעקב ולאה.",
    )
]


def public_questions() -> list[dict]:
    """מחזיר שאלות ללא התשובות הנכונות."""
    return [
        {"id": item.id, "question": item.question, "answers": item.answers}
        for item in TRIVIA_QUESTIONS
    ]


def check_answer(question_id: str, selected_answer: int) -> dict | None:
    question = next((item for item in TRIVIA_QUESTIONS if item.id == question_id), None)
    if question is None:
        return None
    return {
        "is_correct": selected_answer == question.correct_answer,
        "correct_answer": question.correct_answer,
        "explanation": question.explanation,
    }
