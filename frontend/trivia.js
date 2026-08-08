let triviaQuestions = [];
let currentQuestion = 0;
let correctAnswers = 0;
let hasAnswered = false;

function escapeHtml(value) { return value.replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#039;", '"': "&quot;" })[character]); }
function quizTarget() { return document.getElementById("חידון-תוכן"); }

function renderQuestion() {
  const item = triviaQuestions[currentQuestion];
  const progress = ((currentQuestion + 1) / triviaQuestions.length) * 100;
  quizTarget().innerHTML = `<div class="quiz-progress"><span>שאלה ${currentQuestion + 1} מתוך ${triviaQuestions.length}</span><div><i style="width:${progress}%"></i></div></div><h2>${escapeHtml(item.question)}</h2><div class="answers">${item.answers.map((answer, index) => `<button class="answer" data-answer="${index}">${escapeHtml(answer)}</button>`).join("")}</div><p id="תשובת-חידון" class="quiz-result"></p><div id="פעולת-חידון"></div>`;
  hasAnswered = false;
}

async function submitAnswer(button) {
  if (hasAnswered) return;
  hasAnswered = true;
  const item = triviaQuestions[currentQuestion];
  const selected = Number(button.dataset.answer);
  document.querySelectorAll(".answer").forEach(element => element.disabled = true);
  try {
    const response = await fetch(`/api/trivia/${encodeURIComponent(item.id)}/answer`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ selected_answer: selected }) });
    if (!response.ok) throw new Error();
    const result = await response.json();
    if (result.is_correct) correctAnswers += 1;
    button.classList.add(result.is_correct ? "correct" : "incorrect");
    if (!result.is_correct) document.querySelectorAll(".answer")[result.correct_answer].classList.add("correct");
    document.getElementById("תשובת-חידון").textContent = result.is_correct ? result.explanation : `לא בדיוק. ${result.explanation}`;
    const isLast = currentQuestion === triviaQuestions.length - 1;
    document.getElementById("פעולת-חידון").innerHTML = `<button class="next-question" id="הבא">${isLast ? "לצפייה בתוצאה" : "לשאלה הבאה"}</button>`;
  } catch (_) {
    hasAnswered = false;
    document.querySelectorAll(".answer").forEach(element => element.disabled = false);
    document.getElementById("תשובת-חידון").textContent = "לא ניתן לבדוק את התשובה כעת. נסו שוב בעוד רגע.";
  }
}

function showResult() {
  const total = triviaQuestions.length;
  quizTarget().innerHTML = `<div class="quiz-result-screen"><p class="eyebrow">כל הכבוד!</p><h2>סיימתם את החידון</h2><strong>${correctAnswers} מתוך ${total}</strong><p>עניתם נכון על ${correctAnswers} שאלות.</p><button class="next-question" id="התחלה-מחדש">התחילו מחדש</button></div>`;
}

document.addEventListener("click", event => {
  const answer = event.target.closest(".answer"); if (answer) { submitAnswer(answer); return; }
  if (event.target.closest("#הבא")) { currentQuestion += 1; currentQuestion < triviaQuestions.length ? renderQuestion() : showResult(); }
  if (event.target.closest("#התחלה-מחדש")) { currentQuestion = 0; correctAnswers = 0; renderQuestion(); }
});

fetch("/api/trivia").then(response => { if (!response.ok) throw new Error(); return response.json(); }).then(items => { triviaQuestions = items; items.length ? renderQuestion() : quizTarget().innerHTML = "<p>אין כרגע שאלות בחידון.</p>"; }).catch(() => { quizTarget().innerHTML = "<p>לא ניתן לטעון את החידון כעת. נסו לרענן את העמוד.</p>"; });
