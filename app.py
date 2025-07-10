from flask import Flask
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Simulated database
pet_data = {}

# Simulate wearable data
def generate_vitals():
    return {
        "heartRate": random.randint(60, 140),
        "activity": random.randint(1000, 6000),
        "sleep": random.randint(4, 15)
    }

# AI recommendation logic
def get_recommendation(vitals):
    if vitals["heartRate"] > 120:
        return "Consult vet: High heart rate detected."
    if vitals["activity"] < 2000:
        return "Increase exercise: Low activity level."
    return "Pet is healthy! Maintain current routine."

# Alert logic
def get_alert(vitals):
    if vitals["heartRate"] > 130 or vitals["sleep"] < 4:
        return "Urgent: Contact vet immediately!"
    return "No alerts"

@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("status", {"message": "Connected to PetPal backend"})

@socketio.on("request_data")
def handle_request_data():
    while True:
        vitals = generate_vitals()
        recommendation = get_recommendation(vitals)
        alert = get_alert(vitals)
        pet_data["vitals"] = vitals
        pet_data["recommendation"] = recommendation
        pet_data["alert"] = alert
        emit("vitals_update", pet_data)
        time.sleep(2)  # Update every 2 seconds

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)