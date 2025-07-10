<img width="1920" height="1007" alt="PetPal Prototype - Google Chrome 11-07-2025 01_57_52" src="https://github.com/user-attachments/assets/6fb35e38-25ff-488f-b9d9-208fe0035ee9" />
# PetPal Prototype

Welcome to the **PetPal Prototype**, an innovative real-time pet health monitoring and recommendation system designed to enhance pet care through cutting-edge technology. This prototype leverages a web-based interface to display live vitals, provide AI-driven health recommendations, and issue vet alerts, offering a glimpse into the full potential of the PetPal product as outlined in the accompanying report.

## Installation

To get started with the PetPal Prototype, follow these straightforward steps to set up your environment and clone the project:

1. **Ensure Prerequisites**: Install [Node.js](https://nodejs.org/) for the frontend and [Python](https://www.python.org/) for the backend to support the application's real-time features.
2. **Clone the Repository**: Retrieve the project files by running:
   ```bash
   git clone https://github.com/TanishSharma2004/Petpal-project
   ```

3. **Navigate to Project Folder**: Move into the project directory with:
   ```bash
   cd PetPal-Project
   ```
4. **Install Python Dependencies**: Set up the backend by installing required packages:
   ```bash
   pip install flask flask-socketio
   ```
5. **Install HTTP Server (Optional)**: For a seamless frontend experience, install a simple server:
   ```bash
   npm install -g http-server
   ```

## Usage

Once installed, launch the PetPal Prototype with these easy steps to experience real-time pet health monitoring:

1. **Start the Backend Server**: Navigate to the backend folder and run the Flask server:
   ```bash
   cd backend
   python app.py
   ```
   (You’ll see a confirmation message indicating the server is running on `http://0.0.0.0:5000`.)
2. **Launch the Frontend**: In a new terminal, return to the root folder and start the HTTP server:
   ```bash
   cd ..
   npx http-server
   ```
3. **Access the Dashboard**: Open your web browser and visit `http://localhost:8080` (or the port displayed by `http-server`).
4. **Experience Real-Time Updates**: The dashboard will automatically display live vitals (heart rate, activity, sleep), AI-generated recommendations, and vet alerts, updating in real time.

## Features

The PetPal Prototype showcases the following key capabilities, reflecting the vision from the PetPal report:

- **Real-Time Vitals Monitoring**: Tracks and displays live data including heart rate, activity levels, and sleep duration.
- **AI-Based Health Recommendations**: Offers personalized advice (e.g., exercise tips or vet consultations) based on analyzed vitals.
- **Vet Alert System**: Provides critical notifications for urgent health conditions requiring immediate attention.
- **WebSocket Integration**: Ensures seamless, real-time data streaming between the backend and frontend.

## File Structure

Understand the organization of the project with this clear layout:

```
PetPal-Project/
├── backend/
│   └── app.py          # Flask backend with WebSocket for real-time data processing
├── index.html          # Frontend HTML file forming the user interface
├── script.js           # Frontend JavaScript for WebSocket communication and display
├── styles.css          # Frontend CSS for a polished and responsive design
└── petpal_diagram.pdf  # Schematic diagram visualizing the PetPal architecture
```

Join us in making PetPal a leader in pet health technology!

## Sample Capture

---
