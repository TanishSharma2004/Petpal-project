function generateVitals() {
    return {
        heartRate: Math.floor(Math.random() * 100) + 60,
        activity: Math.floor(Math.random() * 5000) + 1000,
        sleep: Math.floor(Math.random() * 12) + 4
    };
}

function generateRecommendation(vitals) {
    if (vitals.heartRate > 120) return "Consult vet: High heart rate detected.";
    if (vitals.activity < 2000) return "Increase exercise: Low activity level.";
    return "Pet is healthy! Maintain current routine.";
}

function generateAlert(vitals) {
    if (vitals.heartRate > 130 || vitals.sleep < 4) return "Urgent: Contact vet immediately!";
    return "No alerts";
}

function updateData() {
    const vitals = generateVitals();
    const recommendation = generateRecommendation(vitals);
    const alert = generateAlert(vitals);

    document.getElementById('heartRate').textContent = vitals.heartRate;
    document.getElementById('activity').textContent = vitals.activity;
    document.getElementById('sleep').textContent = vitals.sleep;
    document.getElementById('recommendation').textContent = recommendation;
    document.getElementById('alert').textContent = alert;
}

updateData();