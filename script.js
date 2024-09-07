document.addEventListener("DOMContentLoaded", () => {
    const textToSpeechButton = document.getElementById("textToSpeech");
    const speechToTextButton = document.getElementById("speechToText");
    const writingPadButton = document.getElementById("writingPad");
    const customizationButton = document.getElementById("customization");

    const textToSpeechModal = document.getElementById("textToSpeechModal");
    const speechToTextModal = document.getElementById("speechToTextModal");
    const customizationModal = document.getElementById("customizationModal");

    const closeTextToSpeech = document.getElementById("closeTextToSpeech");
    const closeSpeechToText = document.getElementById("closeSpeechToText");
    const closeCustomization = document.getElementById("closeCustomization");

    const speakTextButton = document.getElementById("speakText");
    const startSpeechRecognitionButton = document.getElementById(
        "startSpeechRecognition"
    );

    const contrastInput = document.getElementById("contrast");
    const brightnessInput = document.getElementById("brightness");

    textToSpeechButton.addEventListener("click", () => {
        textToSpeechModal.style.display = "block";
    });

    speechToTextButton.addEventListener("click", () => {
        speechToTextModal.style.display = "block";
    });

    writingPadButton.addEventListener("click", () => {
        window.open("writingPad.html", "_blank", "width=800,height=600");
    });

    customizationButton.addEventListener("click", () => {
        customizationModal.style.display = "block";
    });

    closeTextToSpeech.addEventListener("click", () => {
        textToSpeechModal.style.display = "none";
    });

    closeSpeechToText.addEventListener("click", () => {
        speechToTextModal.style.display = "none";
    });

    closeCustomization.addEventListener("click", () => {
        customizationModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
        if (event.target === textToSpeechModal) {
            textToSpeechModal.style.display = "none";
        } else if (event.target === speechToTextModal) {
            speechToTextModal.style.display = "none";
        } else if (event.target === customizationModal) {
            customizationModal.style.display = "none";
        }
    });

    speakTextButton.addEventListener("click", () => {
        const text = document.getElementById("textInput").value;
        if ("speechSynthesis" in window) {
            const utterance = new SpeechSynthesisUtterance(text);
            window.speechSynthesis.speak(utterance);
            // Implement sending text to Arduino or speaker
        } else {
            alert("Text-to-Speech is not supported in this browser.");
        }
    });

    startSpeechRecognitionButton.addEventListener("click", () => {
        if ("webkitSpeechRecognition" in window) {
            const recognition = new webkitSpeechRecognition();
            recognition.lang = "en-US";
            recognition.interimResults = false;
            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                document.getElementById("speechText").innerText = transcript;
            };
            recognition.start();
        } else {
            alert("Speech Recognition is not supported in this browser.");
        }
    });

    contrastInput.addEventListener("input", () => {
        document.body.style.filter = `contrast(${contrastInput.value}) brightness(${brightnessInput.value})`;
    });

    brightnessInput.addEventListener("input", () => {
        document.body.style.filter = `contrast(${contrastInput.value}) brightness(${brightnessInput.value})`;
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const writingPadButton = document.getElementById("writingPad");

    writingPadButton.addEventListener("click", () => {
        // Replace 'http://localhost:5000' with the URL of your Flask server if it's different
        window.open("http://localhost:5000", "_blank", "width=800,height=600");
    });
});
