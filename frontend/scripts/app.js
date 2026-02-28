"use strict";
async function computeFromUI(n) {
  const resp = await fetch('/calculate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ n })
  });
  if (!resp.ok) throw new Error('API error');
  const data = await resp.json();
  return data.result;
}

// Example usage placeholder for integration with a richer frontend
