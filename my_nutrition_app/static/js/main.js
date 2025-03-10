const predictBtn = document.getElementById('predictBtn');
const productInput = document.getElementById('productInput');
const resultsContainer = document.getElementById('resultsContainer');

const caloriesLabel = document.getElementById('caloriesLabel');
const proteinLabel = document.getElementById('proteinLabel');
const carbsLabel = document.getElementById('carbsLabel');
const fatLabel = document.getElementById('fatLabel');

function highlightElement(element) {
  element.classList.remove('highlight');
  void element.offsetWidth;
  element.classList.add('highlight');
}

predictBtn.addEventListener('click', async () => {
  const productName = productInput.value.trim();

  if (!productName) {
    alert('Please enter a product name.');
    return;
  }

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ product_name: productName })
    });

    if (!response.ok) {
      const errData = await response.json();
      alert(errData.error || 'An error occurred while predicting.');
      return;
    }

    const data = await response.json();

    caloriesLabel.textContent = `CALORIES: ${data.Calories.toFixed(2)}`;
    proteinLabel.textContent = `PROTEIN: ${data.Protein.toFixed(2)}`;
    carbsLabel.textContent    = `CARBS: ${data.Carbs.toFixed(2)}`;
    fatLabel.textContent      = `FAT: ${data.Fat.toFixed(2)}`;

    highlightElement(caloriesLabel);
    highlightElement(proteinLabel);
    highlightElement(carbsLabel);
    highlightElement(fatLabel);

  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred. Check console for details.');
  }
});
