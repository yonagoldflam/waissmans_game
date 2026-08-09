let triviaQuestions = [];
let correctAnswers = 0;

function escapeHtml(value) { return value.replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#039;", '"': "&quot;" })[character]); }
function quizTarget() { return document.getElementById("חידון-תוכן"); }

function renderTrivia() {
  quizTarget().innerHTML = `<form id="טופס-חידון">${triviaQuestions.map((item, questionIndex) => `<article class="all-question" data-question="${questionIndex}"><p class="question-count">שאלה ${questionIndex + 1} מתוך ${triviaQuestions.length}</p><h2>${escapeHtml(item.question)}</h2><div class="answers">${item.answers.map((answer, answerIndex) => `<label class="answer"><input type="radio" name="שאלה-${questionIndex}" value="${answerIndex}" required /><span>${escapeHtml(answer)}</span></label>`).join("")}</div><p class="quiz-result"></p></article>`).join("")}<button class="next-question" type="submit">סיום החידון וקבלת תוצאה</button></form>`;
}

async function checkAllAnswers(event) {
  event.preventDefault();
  const form = event.currentTarget;
  if (!form.reportValidity()) return;
  const button = form.querySelector("button[type=submit]");
  button.disabled = true;
  button.textContent = "בודקים תשובות…";
  try {
    const results = await Promise.all(triviaQuestions.map((item, index) => {
      const selected = Number(form.querySelector(`input[name="שאלה-${index}"]:checked`).value);
      return fetch(`/api/trivia/${encodeURIComponent(item.id)}/answer`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ selected_answer: selected }) }).then(response => { if (!response.ok) throw new Error(); return response.json(); });
    }));
    correctAnswers = results.filter(result => result.is_correct).length;
    results.forEach((result, index) => {
      const question = form.querySelector(`[data-question="${index}"]`);
      question.querySelectorAll("input").forEach(input => input.disabled = true);
      const selected = question.querySelector("input:checked").closest(".answer");
      selected.classList.add(result.is_correct ? "correct" : "incorrect");
      if (!result.is_correct) question.querySelector(`input[value="${result.correct_answer}"]`).closest(".answer").classList.add("correct");
      question.querySelector(".quiz-result").textContent = result.is_correct ? result.explanation : `לא בדיוק. ${result.explanation}`;
    });
    button.remove();
    form.insertAdjacentHTML("beforeend", `<div class="quiz-result-screen"><p class="eyebrow">כל הכבוד!</p><h2>סיימתם את החידון</h2><strong>${correctAnswers} מתוך ${triviaQuestions.length}</strong><p>עניתם נכון על ${correctAnswers} שאלות.</p><button class="next-question" type="button" id="התחלה-מחדש">התחילו מחדש</button></div>`);
  } catch (_) { button.disabled = false; button.textContent = "סיום החידון וקבלת תוצאה"; alert("לא ניתן לבדוק את התשובות כעת. נסו שוב בעוד רגע."); }
}

document.addEventListener("submit", event => { if (event.target.id === "טופס-חידון") checkAllAnswers(event); });
document.addEventListener("click", event => { if (event.target.closest("#התחלה-מחדש")) renderTrivia(); });
fetch("/api/trivia").then(response => { if (!response.ok) throw new Error(); return response.json(); }).then(items => { triviaQuestions = items; items.length ? renderTrivia() : quizTarget().innerHTML = "<p>אין כרגע שאלות בחידון.</p>"; }).catch(() => { quizTarget().innerHTML = "<p>לא ניתן לטעון את החידון כעת. נסו לרענן את העמוד.</p>"; });
