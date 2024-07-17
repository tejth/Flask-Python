function validateForm(event) {
  const inputs = document.querySelectorAll('input[type="text"]');
  let valid = true;

  inputs.forEach((input) => {
    if (isNaN(input.value) || input.value < 0) {
      alert(`${input.name} must be a positive number.`);
      valid = false;
    }
  });

  if (!valid) {
    event.preventDefault();
  }
}
