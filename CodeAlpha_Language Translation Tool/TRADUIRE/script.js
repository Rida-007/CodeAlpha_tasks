// Select elements
const fromSelect = document.querySelector(".lang-row select:first-of-type");
const toSelect = document.querySelector(".lang-row select:last-of-type");
const swapBtn = document.querySelector(".swap-btn");

const inputText = document.querySelector(".box textarea");
const outputText = document.querySelector(".output textarea");

const translateBtn = document.querySelector(".translate-btn");

const icons = document.querySelectorAll(".icons i");

//  Swap languages and text
swapBtn.addEventListener("click", () => {
  // swap languages
  const tempLang = fromSelect.value;
  fromSelect.value = toSelect.value;
  toSelect.value = tempLang;

  // swap text
  const tempText = inputText.value;
  inputText.value = outputText.value;
  outputText.value = tempText;
});

//  Translate button 
translateBtn.addEventListener("click", () => {
  const text = inputText.value.trim();

  if (!text) {
    alert("Please enter text to translate");
    return;
  }

  // Dummy translation (replace with API later)
  outputText.value = `🔤 Translated (${toSelect.value}):\n\n${text}`;
});

//  Text-to-Speech &  Copy
icons.forEach(icon => {
  icon.addEventListener("click", () => {
    // SPEAK INPUT
    if (icon.classList.contains("fa-microphone") ||
        icon.classList.contains("fa-volume-high") && icon.closest(".box") && !icon.closest(".output")) {

      speakText(inputText.value, fromSelect.value);
    }

    // SPEAK OUTPUT
    if (icon.classList.contains("fa-volume-high") &&
        icon.closest(".output")) {

      speakText(outputText.value, toSelect.value);
    }

    // COPY OUTPUT
    if (icon.classList.contains("fa-copy")) {
      navigator.clipboard.writeText(outputText.value);
      alert("Copied to clipboard!");
    }

    // STAR (SAVE)
    if (icon.classList.contains("fa-star")) {
      alert("Saved to phrases ⭐ (feature coming soon)");
    }

    // SHARE
    if (icon.classList.contains("fa-share-nodes")) {
      alert("Share feature coming soon 🔗");
    }
  });
});

//  Speech function
function speakText(text, language) {
  if (!text) return;

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = getLangCode(language);
  speechSynthesis.speak(utterance);
}

// Map language names to speech codes
function getLangCode(lang) {
  const map = {
    "English": "en-US",
    "French": "fr-FR",
    "German": "de-DE",
    "Spanish": "es-ES",
    "Italian": "it-IT",
    "Portuguese": "pt-PT",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Malayalam": "ml-IN",
    "Kannada": "kn-IN",
    "Bengali": "bn-IN",
    "Marathi": "mr-IN",
    "Gujarati": "gu-IN",
    "Punjabi": "pa-IN",
    "Urdu": "ur-IN",
    "Arabic": "ar-SA",
    "Japanese": "ja-JP",
    "Korean": "ko-KR",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Russian": "ru-RU",
    "Turkish": "tr-TR",
    "Greek": "el-GR",
    "Hebrew": "he-IL",
    "Thai": "th-TH",
    "Vietnamese": "vi-VN"
  };

  return map[lang] || "en-US";
}
