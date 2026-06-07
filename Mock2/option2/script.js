const recommendationForm = document.getElementById("recommendation-form");
const recommendationInput = document.getElementById("new-recommendation");
const recommendationList = document.getElementById("recommendation-list");
const popup = document.getElementById("popup");
const closePopupButton = document.getElementById("close-popup");

function showPopup() {
  popup.classList.add("show");
}

function hidePopup() {
  popup.classList.remove("show");
}

function addRecommendation(event) {
  event.preventDefault();

  const recommendationText = recommendationInput.value.trim();

  if (recommendationText.length === 0) {
    return;
  }

  const newRecommendation = document.createElement("blockquote");
  newRecommendation.textContent = recommendationText;
  recommendationList.appendChild(newRecommendation);
  recommendationInput.value = "";

  showPopup();
}

recommendationForm.addEventListener("submit", addRecommendation);
closePopupButton.addEventListener("click", hidePopup);
