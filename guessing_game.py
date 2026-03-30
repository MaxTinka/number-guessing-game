"""
Number Guessing Game
Author: Tinka Max
Course: CSE 310 – Applied Programming
Module: Data Analysis / Python

A fun game where the player guesses a random number.
Features difficulty levels, attempt tracking, and high scores.
"""

import random
import json
import os
from datetime import datetime

# File to store high scores
HIGH_SCORES_FILE = "high_scores.json"

# Game settings
DIFFICULTY_SETTINGS = {
    'easy': {
        'name': 'Easy',
        'range_min': 1,
        'range_max': 20,
        'max_attempts': 10,
        'points_per_win': 10
    },
    'medium': {
        'name': 'Medium',
        'range_min': 1,
        'range_max': 50,
        'max_attempts': 7,
        'points_per_win': 20
    },
    'hard': {
        'name': 'Hard',
        'range_min': 1,
        'range_max': 100,
        'max_attempts': 5,
        'points_per_win': 30
    }
}


def load_high_scores():
    """Load high scores from file"""
    if os.path.exists(HIGH_SCORES_FILE):
        try:
            with open(HIGH_SCORES_FILE, 'r') as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_high_scores(scores):
    """Save high scores to file"""
    with open(HIGH_SCORES_FILE, 'w') as file:
        json.dump(scores, file, indent=2)


def update_high_score(player_name, difficulty, score, attempts):
    """Update high score for a player"""
    scores = load_high_scores()
    
    key = f"{player_name}_{difficulty}"
    
    if key not in scores:
        scores[key] = {
            'player': player_name,
            'difficulty': difficulty,
            'score': score,
            'attempts': attempts,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    elif score > scores[key]['score']:
        scores[key]['score'] = score
        scores[key]['attempts'] = attempts
        scores[key]['date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    save_high_scores(scores)


def display_high_scores():
    """Display top high scores"""
    scores = load_high_scores()
    
    if not scores:
        print("\nNo high scores yet. Be the first to set a record!")
        return
    
    # Sort scores by score (highest first)
    sorted_scores = sorted(scores.values(), key=lambda x: x['score'], reverse=True)
    
    print("\n" + "=" * 60)
    print("🏆 HIGH SCORES 🏆")
    print("=" * 60)
    print(f"{'Player':<15} {'Difficulty':<10} {'Score':<8} {'Attempts':<10} {'Date':<20}")
    print("-" * 60)
    
    for i, score in enumerate(sorted_scores[:10], 1):
        print(f"{score['player']:<15} {score['difficulty']:<10} {score['score']:<8} "
              f"{score['attempts']:<10} {score['date']:<20}")
    print("=" * 60)


def get_player_name():
    """Get player name"""
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")
    print("=" * 50)
    
    while True:
        name = input("\nWhat's your name? ").strip()
        if name:
            return name
        print("Please enter a valid name.")


def choose_difficulty():
    """Let player choose difficulty level"""
    print("\n" + "-" * 40)
    print("SELECT DIFFICULTY LEVEL")
    print("-" * 40)
    
    print("\n1. Easy (1-20, 10 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 5 attempts)")
    print("4. View High Scores")
    
    while True:
        choice = input("\nEnter 1, 2, 3, or 4: ").strip()
        
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        elif choice == '4':
            display_high_scores()
            # Continue to ask for difficulty after showing scores
            print("\n" + "-" * 40)
            print("SELECT DIFFICULTY LEVEL")
            print("-" * 40)
            print("\n1. Easy (1-20, 10 attempts)")
            print("2. Medium (1-50, 7 attempts)")
            print("3. Hard (1-100, 5 attempts)")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def give_hint(guess, secret, attempts_remaining):
    """Give a hint based on the guess"""
    if abs(guess - secret) <= 5:
        if guess < secret:
            print("🔥 Hot! You're very close! Go a bit higher.")
        else:
            print("🔥 Hot! You're very close! Go a bit lower.")
    elif abs(guess - secret) <= 10:
        if guess < secret:
            print("🌡️ Warm! Getting closer. Try higher.")
        else:
            print("🌡️ Warm! Getting closer. Try lower.")
    else:
        if guess < secret:
            print("❄️ Cold! Too low. Think bigger!")
        else:
            print("❄️ Cold! Too high. Think smaller!")
    
    print(f"💡 You have {attempts_remaining} attempts remaining.")


def play_game(player_name, difficulty):
    """Main game logic"""
    settings = DIFFICULTY_SETTINGS[difficulty]
    
    secret = random.randint(settings['range_min'], settings['range_max'])
    attempts = 0
    attempts_remaining = settings['max_attempts']
    
    print("\n" + "=" * 50)
    print(f"🎯 {settings['name'].upper()} MODE")
    print("=" * 50)
    print(f"\nI'm thinking of a number between {settings['range_min']} and {settings['range_max']}.")
    print(f"You have {settings['max_attempts']} attempts to guess it!")
    
    while attempts < settings['max_attempts']:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{settings['max_attempts']}: Guess a number: "))
            attempts += 1
            attempts_remaining = settings['max_attempts'] - attempts
            
            if guess < settings['range_min'] or guess > settings['range_max']:
                print(f"⚠️ Please guess between {settings['range_min']} and {settings['range_max']}.")
                continue
            
            if guess < secret:
                print("📉 Too low!", end=" ")
                give_hint(guess, secret, attempts_remaining)
            elif guess > secret:
                print("📈 Too high!", end=" ")
                give_hint(guess, secret, attempts_remaining)
            else:
                # Correct guess!
                score = settings['points_per_win'] * (settings['max_attempts'] - attempts + 1)
                print("\n" + "🎉" * 10)
                print(f"🎉 CONGRATULATIONS, {player_name}! 🎉")
                print("🎉" * 10)
                print(f"\nYou guessed the number {secret} in {attempts} attempts!")
                print(f"Your score: {score} points!")
                
                # Update high score
                update_high_score(player_name, difficulty, score, attempts)
                
                return True, score, attempts
                
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Game over - out of attempts
    print("\n" + "💀" * 10)
    print(f"💀 GAME OVER, {player_name}! 💀")
    print("💀" * 10)
    print(f"\nThe number was {secret}.")
    print("Better luck next time!")
    
    return False, 0, attempts


def show_game_stats(player_name, games_played, total_score, best_game):
    """Display player statistics"""
    print("\n" + "=" * 50)
    print("📊 YOUR STATISTICS")
    print("=" * 50)
    print(f"Player: {player_name}")
    print(f"Games Played: {games_played}")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {total_score / games_played:.1f}" if games_played > 0 else "Average Score: 0")
    if best_game:
        print(f"Best Game: {best_game['score']} points in {best_game['attempts']} attempts")
    print("=" * 50)


def main():
    """Main game loop"""
    player_name = get_player_name()
    
    games_played = 0
    total_score = 0
    best_game = None
    
    while True:
        difficulty = choose_difficulty()
        
        # If user selected to view scores, continue to ask for difficulty
        if difficulty is None:
            continue
            
        # Play the game
        won, score, attempts = play_game(player_name, difficulty)
        
        games_played += 1
        total_score += score
        
        if won and (best_game is None or score > best_game['score']):
            best_game = {'score': score, 'attempts': attempts}
        
        # Ask if player wants to play again
        print("\n" + "-" * 40)
        play_again = input("Play again? (y/n): ").strip().lower()
        
        if play_again != 'y':
            break
    
    # Show final statistics
    show_game_stats(player_name, games_played, total_score, best_game)
    
    # Show high scores
    display_high_scores()
    
    print("\n" + "=" * 50)
    print("Thanks for playing! Come back soon! 🎮")
    print("=" * 50)


if __name__ == "__main__":
    main()
