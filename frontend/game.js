const gameId = new URLSearchParams(location.search).get("game");
async function loadGame() {
  const response = await fetch("/api/games"); const games = await response.json(); const game = games.find(item => item.id === gameId);
  const target = document.querySelector("#game-content");
  if (!game) { target.innerHTML = "<h1>Game not found</h1><a class='button button-primary' href='index.html#games'>Return to games</a>"; return; }
  document.title = `${game.title} | Our Family Journey`;
  target.innerHTML = `<div class="game-symbol large ${game.accent}">${({quiz:"?",hunt:"⌕",riddle:"✦"})[game.accent]}</div><h1>${game.title}</h1><p class="lead">${game.description}</p>${game.is_started ? `<div class="game-live"><span>● Live now</span><h2>The game has begun!</h2><p>The rules and interactive experience for this game will appear here.</p></div>` : `<div class="waiting"><span>◌ Waiting room</span><h2>Get ready to play</h2><p>This game will open when the trip administrator starts it. Keep this page open—we will check again in a few seconds.</p></div>`}`;
  if (!game.is_started) setTimeout(loadGame, 5000);
}
loadGame();
