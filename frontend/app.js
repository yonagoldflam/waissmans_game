const api = "/api";
let adminPassword = "";

const gameIcon = { quiz: "?", hunt: "⌕", riddle: "✦" };
function gameCard(game) {
  const status = game.is_started ? "Now playing" : "Waiting to start";
  return `<article class="game-card ${game.accent}"><div class="game-symbol">${gameIcon[game.accent]}</div><span class="status ${game.is_started ? "active" : ""}">${status}</span><h3>${game.title}</h3><p>${game.description}</p><a href="game.html?game=${game.id}">Open game <span>→</span></a></article>`;
}
async function loadGames() {
  const response = await fetch(`${api}/games`);
  if (!response.ok) throw new Error("Could not reach the game server.");
  const games = await response.json();
  document.querySelector("#games-grid").innerHTML = games.map(gameCard).join("");
  if (adminPassword) renderAdmin(games);
}
function renderAdmin(games) {
  document.querySelector("#admin-controls").hidden = false;
  document.querySelector("#admin-controls").innerHTML = `<div class="controls-list">${games.map(game => `<div class="control-row"><div><strong>${game.title}</strong><span>${game.is_started ? "Currently live" : "Waiting"}</span></div><button class="button ${game.is_started ? "button-outline" : "button-primary"}" data-game="${game.id}" data-state="${!game.is_started}">${game.is_started ? "Reset game" : "Start game"}</button></div>`).join("")}</div>`;
}
document.querySelector("#admin-login").addEventListener("submit", async (event) => {
  event.preventDefault(); adminPassword = document.querySelector("#admin-password").value;
  document.querySelector("#login-message").textContent = "Controls unlocked for this page.";
  await loadGames();
});
document.querySelector("#admin-controls").addEventListener("click", async (event) => {
  const button = event.target.closest("button[data-game]"); if (!button) return;
  const response = await fetch(`${api}/games/${button.dataset.game}/state`, { method: "POST", headers: { "Content-Type": "application/json", "X-Admin-Password": adminPassword }, body: JSON.stringify({ is_started: button.dataset.state === "true" }) });
  if (response.status === 401) { document.querySelector("#login-message").textContent = "That password was not accepted."; adminPassword = ""; return; }
  await loadGames();
});
document.querySelector(".menu-toggle").addEventListener("click", event => { const nav = document.querySelector(".main-nav"); nav.classList.toggle("open"); event.currentTarget.setAttribute("aria-expanded", nav.classList.contains("open")); });
loadGames().catch(error => { document.querySelector("#games-grid").innerHTML = `<p class="error">${error.message}</p>`; });
