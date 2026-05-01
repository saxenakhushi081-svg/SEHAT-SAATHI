async function analyzeSymptoms() {
    const symptoms = document.getElementById("symptom-input").value;
    const spinner = document.getElementById("spinner");
    const btnText = document.getElementById("btn-text");

    if (!symptoms) return alert("Bhai, symptoms toh likho!");

    spinner.style.display = "inline-block";
    btnText.textContent = "Analyzing...";

    try{
    const res = await fetch("/api/analyze", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        symptoms,
        age: document.getElementById("age-input").value || null,
        language: document.getElementById("lang-input").value
    })
});

        const response = await fetch("http://127.0.0.1:8000/api/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        symptoms: symptoms,
        age: document.getElementById("age-input").value || null,
        language: document.getElementById("lang-input").value || "English"
    })
});

if (!response.ok) {
    throw new Error("API failed");
}


const data = await response.json();

        // IMPORTANT: correct IDs from your HTML
        document.getElementById("input-section").style.display = "none";
        document.getElementById("results-panel").style.display = "block";

        document.getElementById("res-specialist").textContent = data.specialist;
        document.getElementById("res-icon").textContent = data.specialist_icon;
        document.getElementById("res-reasoning").textContent = data.reasoning;
        document.getElementById("res-severity").textContent = data.severity || "medium";

        // doctors
        const docsContainer = document.getElementById("doctor-list");
        docsContainer.innerHTML = "";

        (data.doctors_nearby || []).forEach(doc => {
            docsContainer.innerHTML += `
                <div class="doctor-card">
                    <div class="doc-name">👨‍⚕️ ${doc.name}</div>
                    <div class="doc-details">Fee: ${doc.fee} | Wait: ${doc.wait}</div>
                    <button class="book-btn">Book</button>
                </div>
            `;
        });

    } catch (e) {
        console.error(e);
        alert("Server error. Check backend terminal.");
    } finally {
        spinner.style.display = "none";
        btnText.textContent = "Analyze Symptoms";
    }
}
