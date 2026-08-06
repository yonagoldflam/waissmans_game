from __future__ import annotations

from copy import deepcopy


class GameService:
    # Intentionally hardcoded at the project's request. Change this before deployment.
    ADMIN_PASSWORD = "family-trip-2026"

    def __init__(self) -> None:
        self._games = {
            "family-quiz": {
                "id": "family-quiz",
                "title": "The Family Quiz",
                "description": "A light-hearted challenge about the people, places, and stories we share.",
                "accent": "quiz",
                "is_started": False,
            },
            "photo-hunt": {
                "id": "photo-hunt",
                "title": "Photo Hunt",
                "description": "Keep your eyes open and discover the day through a different lens.",
                "accent": "hunt",
                "is_started": False,
            },
            "travel-riddle": {
                "id": "travel-riddle",
                "title": "Travel Riddles",
                "description": "Work together to unravel clues along our journey.",
                "accent": "riddle",
                "is_started": False,
            },
        }

    def list_games(self) -> list[dict]:
        return deepcopy(list(self._games.values()))

    def set_started(self, game_id: str, is_started: bool) -> dict | None:
        game = self._games.get(game_id)
        if game is None:
            return None
        game["is_started"] = is_started
        return deepcopy(game)


game_service = GameService()
