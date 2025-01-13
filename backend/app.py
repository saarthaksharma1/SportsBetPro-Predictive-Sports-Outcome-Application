from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Retrieve the API key from the .env file
SOCCER_API_KEY = os.getenv('SOCCER_API_KEY')

# Base URL for API-Football
BASE_URL = 'https://v3.football.api-sports.io'

# Example endpoint to fetch soccer leagues
@app.route('/leagues', methods=['GET'])
def get_leagues():
    headers = {
        'x-rapidapi-key': SOCCER_API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    response = requests.get(f'{BASE_URL}/leagues', headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data', 'status_code': response.status_code})

if __name__ == '__main__':
    app.run(debug=True)
