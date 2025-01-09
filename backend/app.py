from flask import Flask, jsonify
from flask_cors import CORS

import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Connect to the database
def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

@app.route('/')
def index():
    return jsonify({"message": "Welcome to SportsBetPro!"})

@app.route('/api/games', methods=['GET'])
def get_games():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games;")
    games = cursor.fetchall()
    conn.close()

    # Format data for frontend
    games_list = [
        {
            "game_id": row[0],
            "sport_name": row[1],
            "team_a": row[2],
            "team_b": row[3],
            "game_date": row[4],
            "odds_team_a": float(row[5]),
            "odds_team_b": float(row[6]),
            "predicted_winner": row[7],
        }
        for row in games
    ]
    return jsonify(games_list)

if __name__ == '__main__':
    app.run(debug=True)
