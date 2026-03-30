# Number Guessing Game – Data Analysis with Python

## Description
A fun number guessing game with built-in data analysis. The game tracks player performance across difficulty levels and provides statistical insights using pandas and matplotlib.

## GitHub Repository
[https://github.com/maxtinka/number-guessing-game](https://github.com/maxtinka/number-guessing-game)

---

## Dataset
The game creates and analyzes data in `game_sessions.csv` with the following fields:

| Column | Description |
|:---|:---|
| **Date** | Date of the game session |
| **Player** | Player name |
| **Difficulty** | Easy, Medium, or Hard |
| **Secret_Number** | The number to guess |
| **Attempts** | Number of guesses taken |
| **Score** | Points earned |
| **Won** | Whether the player won (Yes/No) |

---

## Analytical Questions

### Question 1: Which difficulty level yields the highest average score?
Analyzes mean scores across Easy, Medium, and Hard difficulty levels.

### Question 2: Does having fewer attempts lead to higher scores?
Examines the correlation between attempts and scores.

### Question 3: What is the win rate for each difficulty level?
Calculates success percentage per difficulty.

---

## Features

### Game Features
- Three difficulty levels: Easy (1-20, 10 attempts), Medium (1-50, 7 attempts), Hard (1-100, 5 attempts)
- Hot/cold hint system with feedback
- Scoring system based on difficulty and remaining attempts
- High score tracking with JSON file
- Game session logging to CSV for analysis

### Data Analysis Features
- Statistical analysis with pandas (averages, correlation, win rates)
- Data visualizations with matplotlib (bar charts)
- Filtering and aggregation by difficulty
- Graphs saved as PNG files

---

## Technologies Used

| Technology | Purpose |
|:---|:---|
| Python 3 | Programming language |
| random | Random number generation |
| json | High score storage |
| csv | Game session logging |
| pandas | Data manipulation and analysis |
| matplotlib | Data visualization |
| datetime | Timestamp tracking |

---

## How to Run

### Option 1: Run on Replit (Recommended – No Installation)

1. Go to [replit.com](https://replit.com)
2. Create a new Python repl
3. Copy all files from this repository into your repl
4. Click **Run** on `guessing_game.py` to play
5. Click **Run** on `analyze_data.py` to see statistics and graphs

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/maxtinka/number-guessing-game.git
cd number-guessing-game

# Install required libraries
pip install pandas matplotlib

# Run the game
python guessing_game.py

# Run data analysis
python analyze_data.py
