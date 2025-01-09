import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [games, setGames] = useState([]);

  // Fetch games data from the backend
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/games") // Backend API endpoint
      .then((response) => {
        setGames(response.data);
      })
      .catch((error) => {
        console.error("Error fetching games data:", error);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>SportsBetPro - Predictive Sports Outcome</h1>
      <h2>Games List</h2>
      {games.length > 0 ? (
        <ul>
          {games.map((game) => (
            <li key={game.game_id}>
              <strong>{game.sport_name}</strong>: {game.team_a} vs {game.team_b} <br />
              Date: {new Date(game.game_date).toLocaleString()} <br />
              Odds: {game.odds_team_a} (Team A) vs {game.odds_team_b} (Team B) <br />
              Predicted Winner: <strong>{game.predicted_winner}</strong>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading games...</p>
      )}
    </div>
  );
}

export default App;
