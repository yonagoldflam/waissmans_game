from __future__ import annotations

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.games import game_service

app = FastAPI(title="Waissman Family Trip API", version="1.0.0")

# Nginx serves the frontend in production. This also makes local frontend
# development convenient when it runs from another port.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-Admin-Password"],
)


class GameStateUpdate(BaseModel):
    is_started: bool


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/games")
def list_games() -> list[dict]:
    return game_service.list_games()


@app.post("/api/games/{game_id}/state")
def update_game_state(game_id: str, update: GameStateUpdate, x_admin_password: str = "") -> dict:
    """Start or reset a game. Authentication is intentionally minimal for this private event."""
    if x_admin_password != game_service.ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Incorrect admin password")

    game = game_service.set_started(game_id, update.is_started)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)