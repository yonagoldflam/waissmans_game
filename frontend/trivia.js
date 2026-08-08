let triviaQuestions = [];
let currentQuestion = 0;

function escapeHtml(value) {
  return value.replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#039;", '"': "&quot;" })[character]);
}

function renderTrivia() {
  const target = document.getElementById("חידון-תוכן");
  const item = triviaQuestions[currentQuestion];
  if (!item) { target.innerHTML = "<p>אין כרגע שאלות בחידון.</p>"; return; }
  target.innerHTML = `<p class="question-count">שאלה ${currentQuestion + 1} מתוך ${triviaQuestions.length}</p><h3>${escapeHtml(item.question)}</h3><div class="answers">${item.answers.map((answer, index) => `<button class="answer" data-answer="${index}">${escapeHtml(answer)}</button>`).join("")}</div><p id="תשובת-חידון" class="quiz-result"></p>`;
}

async function submitAnswer(button) {
  const item = triviaQuestions[currentQuestion];
  const selected = Number(button.dataset.answer);
  document.querySelectorAll(".answer").forEach(element => element.disabled = true);
  try {
    const response = await fetch(`/api/trivia/${encodeURIComponent(item.id)}/answer`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ selected_answer: selected }) });
    if (!response.ok) throw new Error();
    const result = await response.json();
    button.classList.add(result.is_correct ? "correct" : "incorrect");
    if (!result.is_correct) document.querySelectorAll(".answer")[result.correct_answer].classList.add("correct");
    document.getElementById("תשובת-חידון").textContent = result.is_correct ? result.explanation : `לא בדיוק. ${result.explanation}`;
  } catch (_) {
    document.querySelectorAll(".answer").forEach(element => element.disabled = false);
    document.getElementById("תשובת-חידון").textContent = "לא ניתן לבדוק את התשובה כעת. נסו שוב בעוד רגע.";
  }
}

document.addEventListener("click", event => { const button = event.target.closest(".answer"); if (button) submitAnswer(button); });
fetch("/api/trivia").then(response => { if (!response.ok) throw new Error(); return response.json(); }).then(items => { triviaQuestions = items; renderTrivia(); }).catch(() => { document.getElementById("חידון-תוכן").innerHTML = "<p>לא ניתן לטעון את החידון כעת. נסו לרענן את העמוד.</p>"; });
