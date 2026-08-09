from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

from app.trivia import check_answer, public_questions

import logging

app = FastAPI(title="מסע קבר רחל ומערת המכפלה", version="1.1.0")


class TriviaAnswer(BaseModel):
    selected_answer: int


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/trivia")
def get_trivia(response: Response) -> list[dict]:
    logging.info("getting trivia answer")
    # השאלות קבועות; המטמון מפחית עומס גם כאשר משתמשים רבים נכנסים במקביל.
    response.headers["Cache-Control"] = "public, max-age=60"
    return public_questions()


@app.post("/api/trivia/{question_id}/answer")
def submit_trivia_answer(question_id: str, answer: TriviaAnswer) -> dict:
    result = check_answer(question_id, answer.selected_answer)
    if result is None:
        raise HTTPException(status_code=404, detail="השאלה לא נמצאה")
    return result
