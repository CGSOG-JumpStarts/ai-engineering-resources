'use strict';
const form = document.getElementById('advisor-form');
const question = document.getElementById('question');
const submit = document.getElementById('submit');
const count = document.getElementById('character-count');
const result = document.getElementById('result');
const status = document.getElementById('status');
const answer = document.getElementById('answer');
const sources = document.getElementById('sources');
const requestId = document.getElementById('request-id');
question.addEventListener('input', () => { count.textContent = `${question.value.length} / 280 characters`; });
document.querySelectorAll('.example').forEach(button => button.addEventListener('click', () => {
  question.value = button.dataset.question;
  question.dispatchEvent(new Event('input'));
  question.focus();
}));
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  submit.disabled = true;
  result.hidden = false;
  status.textContent = 'Checking';
  answer.textContent = 'Looking up the approved synthetic reference.';
  sources.textContent = '';
  requestId.textContent = '';
  try {
    const response = await fetch('/v1/advice', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({question:question.value})});
    const payload = await response.json();
    status.textContent = response.ok ? payload.status : 'Input error';
    answer.textContent = response.ok ? payload.answer : `Request rejected: ${payload.error || 'unknown_error'}`;
    sources.textContent = payload.source_ids?.length ? `Fictional references: ${payload.source_ids.join(', ')}` : 'No approved reference used.';
    requestId.textContent = payload.request_id ? `Request ${payload.request_id.slice(0, 10)}` : '';
  } catch {
    status.textContent = 'Unavailable';
    answer.textContent = 'Cannot reach the local lab server. Check that it is running.';
  } finally { submit.disabled = false; }
});
