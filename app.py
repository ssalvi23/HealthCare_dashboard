from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

# Initialize Flask app
app = Flask(__name__)

# Sample user data
mock_user_data = {
    "name": "Sakshi",
    "age": 32,
    "lastScreening": "2023-05-15",  # Last screening date
    "oralHealthScore": 78,  # Overall health score
    "screeningHistory": [  # Monthly screening history
        {"date": "2023-01", "score": 65},
        {"date": "2023-02", "score": 68},
        {"date": "2023-03", "score": 72},
        {"date": "2023-04", "score": 75},
        {"date": "2023-05", "score": 78},
    ],
    "upcomingAppointment": "2023-07-01",  # Next appointment
    "dailyHabits": {  # Daily habits
        "brushing": 2,
        "flossing": 1,
        "mouthwash": 1,
    }
}

# Sample screening results data
mock_screening_results = {
    "oralCancer": {"risk": "Low", "score": 2},
    "gumDisease": {"risk": "Moderate", "score": 5},
    "cavities": {"risk": "Low", "score": 3},
    "teethAlignment": {"risk": "High", "score": 8}
}

# Home page route
@app.route('/')
def index():
    return render_template('index.html', user_data=mock_user_data, screening_results=mock_screening_results)

# Route to update age
@app.route('/update_age', methods=['POST'])
def update_age():
    new_age = request.json.get('age')
    mock_user_data['age'] = int(new_age)
    return jsonify({"success": True})

# Route to process a new selfie upload
@app.route('/upload_selfie', methods=['POST'])
def upload_selfie():
    import time
    time.sleep(2)  # Simulate processing delay

    # Update oral health score and screening history
    mock_user_data['oralHealthScore'] = min(100, mock_user_data['oralHealthScore'] + random.randint(1, 5))
    mock_user_data['lastScreening'] = datetime.now().strftime("%Y-%m-%d")
    mock_user_data['screeningHistory'].append({
        "date": datetime.now().strftime("%Y-%m"),
        "score": mock_user_data['oralHealthScore']
    })

    # Generate new screening results
    new_results = {
        "oralCancer": {"risk": "Low", "score": random.randint(1, 3)},
        "gumDisease": {"risk": "Moderate", "score": random.randint(4, 6)},
        "cavities": {"risk": "Low", "score": random.randint(1, 3)},
        "teethAlignment": {"risk": "High", "score": random.randint(7, 10)}
    }

    return jsonify({
        "user_data": mock_user_data,
        "screening_results": new_results
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
