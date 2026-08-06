# Waissman Family Trip

A small FastAPI API with a static, responsive frontend for a one-day family trip.

## Run locally

Create a virtual environment, install requirements, and start the API:

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\uvicorn app.main:app --reload
```

Serve `frontend/` from a static server, or deploy it with Nginx using `nginx.conf.example`. The API defaults to `http://127.0.0.1:8000`; in production Nginx proxies `/api/` to it.

## Editing the trip

- Change the admin password in `app/services/games.py` before deployment.
- Add or edit games in `GameService._games`.
- Replace the two files in `frontend/content/` with the historical copy.
- Implement a game's specific experience in `frontend/game.html` / `frontend/game.js`, using the game ID as the extension point.

## Deploy

Run `docker compose up -d --build`, copy the repository's `frontend/` and `logo/` folders to the Nginx web root indicated in the example configuration, then enable the Nginx site.
