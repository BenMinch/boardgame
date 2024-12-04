document.addEventListener("DOMContentLoaded", () => {
  const buttons = ["animalTrivia", "bibleSwordDrill", "bibleTrivia", "randomTrivia", "fillInBlank", "pictionary"];
  const output = document.getElementById("output");

  buttons.forEach(button => {
    document.getElementById(button).addEventListener("click", () => {
      fetch(`/getPrompt/${button}`)
        .then(response => response.json())
        .then(data => {
          output.textContent = data.error || data.prompt;
        })
        .catch(err => {
          output.textContent = "Error fetching data.";
        });
    });
  });
});
