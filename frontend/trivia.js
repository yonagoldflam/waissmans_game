let triviaQuestions = [];
let correctAnswers = 0;
let answeredQuestions = 0;

function escapeHtml(value) { return value.replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#039;", '"': "&quot;" })[character]); }
function quizTarget() { return document.getElementById("חידון-תוכן"); }

function renderTrivia() {
  correctAnswers = 0;
  answeredQuestions = 0;
  quizTarget().innerHTML = `<div id="ציון-ביניים" class="live-score">עניתם על 0 מתוך ${triviaQuestions.length} שאלות</div>${triviaQuestions.map((item, questionIndex) => `<article class="all-question" data-question="${questionIndex}"><p class="question-count">שאלה ${questionIndex + 1} מתוך ${triviaQuestions.length}</p><h2>${escapeHtml(item.question)}</h2><div class="answers">${item.answers.map((answer, answerIndex) => `<button class="answer" data-question="${questionIndex}" data-answer="${answerIndex}">${escapeHtml(answer)}</button>`).join("")}</div><p class="quiz-result"></p></article>`).join("")}<div id="תוצאה-סופית"></div>`;
}

async function submitAnswer(button) {
  const questionIndex = Number(button.dataset.question);
  const question = button.closest(".all-question");
  if (question.dataset.answered === "true") return;
  question.dataset.answered = "true";
  question.querySelectorAll(".answer").forEach(element => element.disabled = true);
  try {
    const response = await fetch(`/api/trivia/${encodeURIComponent(triviaQuestions[questionIndex].id)}/answer`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ selected_answer: Number(button.dataset.answer) }) });
    if (!response.ok) throw new Error();
    const result = await response.json();
    answeredQuestions += 1;
    if (result.is_correct) correctAnswers += 1;
    button.classList.add(result.is_correct ? "correct" : "incorrect");
    if (!result.is_correct) question.querySelectorAll(".answer")[result.correct_answer].classList.add("correct");
    question.querySelector(".quiz-result").textContent = result.is_correct ? result.explanation : `לא בדיוק. ${result.explanation}`;
    document.getElementById("ציון-ביניים").textContent = `עניתם על ${answeredQuestions} מתוך ${triviaQuestions.length} שאלות · ${correctAnswers} תשובות נכונות`;
    if (answeredQuestions === triviaQuestions.length) showResult();
  } catch (_) {
    question.dataset.answered = "false";
    question.querySelectorAll(".answer").forEach(element => element.disabled = false);
    question.querySelector(".quiz-result").textContent = "לא ניתן לבדוק את התשובה כעת. נסו שוב בעוד רגע.";
  }
}

function showResult() { document.getElementById("תוצאה-סופית").innerHTML = `<div class="quiz-result-screen"><p class="eyebrow">כל הכבוד!</p><h2>סיימתם את החידון</h2><strong>${correctAnswers} מתוך ${triviaQuestions.length}</strong><p>עניתם נכון על ${correctAnswers} שאלות.</p><button class="next-question" type="button" id="התחלה-מחדש">התחילו מחדש</button></div>`; }
document.addEventListener("click", event => { const answer = event.target.closest(".answer"); if (answer) submitAnswer(answer); if (event.target.closest("#התחלה-מחדש")) renderTrivia(); });
fetch("/api/trivia").then(response => { if (!response.ok) throw new Error(); return response.json(); }).then(items => { triviaQuestions = items; items.length ? renderTrivia() : quizTarget().innerHTML = "<p>אין כרגע שאלות בחידון.</p>"; }).catch(() => { quizTarget().innerHTML = "<p>לא ניתן לטעון את החידון כעת. נסו לרענן את העמוד.</p>"; });
