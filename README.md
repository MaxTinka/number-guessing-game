# Number Guessing Game – Data Analysis with Python

## Description
A fun number guessing game with built-in data analysis. The game tracks player performance across difficulty levels and provides statistical insights.

## Dataset
The game creates and analyzes data in `game_sessions.csv` with the following fields:
- **Date** – Date of the game session
- **Player** – Player name
- **Difficulty** – Easy, Medium, or Hard
- **Secret_Number** – The number to guess
- **Attempts** – Number of guesses taken
- **Score** – Points earned
- **Won** – Whether the player won

## Analytical Questions
1. **Which difficulty level yields the highest average score?**
   - Analyzes mean scores across Easy, Medium, and Hard
   - Helps players choose the most rewarding difficulty

2. **Does having fewer attempts lead to higher scores?**
   - Examines correlation between attempts and scores
   - Tests if efficiency in guessing improves outcomes

3. **What is the win rate for each difficulty level?**
   - Calculates success percentage per difficulty
   - Shows which difficulty is easiest to win

## Features
- Three difficulty levels (Easy: 1-20, Medium: 1-50, Hard: 1-100)
- Hot/cold hint system
- Scoring system based on difficulty and remaining attempts
- High score tracking with JSON file
- **Data analysis with pandas** – statistical insights
- **Graphical visualization** – bar charts of scores and win rates

## How to Run

### Run the Game:
```bash
python guessing_game.py
