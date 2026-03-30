"""
Data Analysis Module - Game Session Analysis
Author: Tinka Max
Course: CSE 310 – Applied Programming
Module: Data Analysis

Analyzes game data from the Number Guessing Game using pandas and matplotlib.
Answers three analytical questions and creates visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def analyze_game_data():
    """Load game sessions and perform comprehensive data analysis"""
    
    # Check if dataset exists
    if not os.path.exists('game_sessions.csv'):
        print("❌ No game data found. Please play a few games first.")
        print("   Run guessing_game.py to create game sessions.")
        return None, None, None
    
    # Load dataset
    df = pd.read_csv('game_sessions.csv')
    
    print("\n" + "=" * 60)
    print("📊 GAME SESSION ANALYSIS REPORT")
    print("=" * 60)
    
    print("\n--- Dataset Overview ---")
    print(f"Total Game Sessions: {len(df)}")
    print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"Players: {df['Player'].nunique()}")
    print(f"Difficulties: {', '.join(df['Difficulty'].unique())}")
    
    # ============================================
    # QUESTION 1: Which difficulty level yields the highest average score?
    # ============================================
    print("\n" + "=" * 50)
    print("QUESTION 1: Which difficulty level yields the highest average score?")
    print("=" * 50)
    
    avg_score_by_difficulty = df.groupby('Difficulty')['Score'].mean().round(2)
    print("\nAverage Score by Difficulty:")
    for diff, score in avg_score_by_difficulty.items():
        print(f"  {diff}: {score} points")
    
    best_difficulty = avg_score_by_difficulty.idxmax()
    best_score = avg_score_by_difficulty.max()
    print(f"\n✅ ANSWER: {best_difficulty.capitalize()} difficulty yields the highest average score ({best_score} points)")
    print("   Justification: Calculated by grouping game sessions by difficulty and computing mean score.")
    
    # ============================================
    # QUESTION 2: Does having fewer attempts lead to higher scores?
    # ============================================
    print("\n" + "=" * 50)
    print("QUESTION 2: Does having fewer attempts lead to higher scores?")
    print("=" * 50)
    
    # Filter only won games
    won_games = df[df['Won'] == 'Yes']
    
    if len(won_games) > 0:
        correlation = won_games['Attempts'].corr(won_games['Score'])
        print(f"\nCorrelation between Attempts and Score: {correlation:.3f}")
        
        if correlation < -0.5:
            print("\n✅ ANSWER: Yes, there is a strong negative correlation.")
            print("   Fewer attempts strongly correlate with higher scores.")
            print("   Justification: Pearson correlation coefficient = {:.3f}".format(correlation))
        elif correlation < -0.2:
            print("\n✅ ANSWER: Yes, there is a moderate negative correlation.")
            print("   Fewer attempts tend to result in higher scores.")
            print("   Justification: Pearson correlation coefficient = {:.3f}".format(correlation))
        else:
            print("\n✅ ANSWER: No, there is no clear relationship.")
            print("   Attempts do not strongly predict scores.")
            print("   Justification: Pearson correlation coefficient = {:.3f}".format(correlation))
        
        # Show sorted data
        won_games_sorted = won_games.sort_values('Attempts')
        print("\n   Sample data (sorted by attempts):")
        for _, row in won_games_sorted.head(5).iterrows():
            print(f"   {row['Difficulty']}: {row['Attempts']} attempts → {row['Score']} points")
    else:
        print("\nNo won games to analyze.")
    
    # ============================================
    # QUESTION 3: What is the win rate for each difficulty level?
    # ============================================
    print("\n" + "=" * 50)
    print("QUESTION 3: What is the win rate for each difficulty level?")
    print("=" * 50)
    
    win_rates = df.groupby('Difficulty').apply(
        lambda x: (x['Won'] == 'Yes').sum() / len(x) * 100
    ).round(1)
    
    print("\nWin Rate by Difficulty:")
    for diff, rate in win_rates.items():
        print(f"  {diff}: {rate}%")
    
    best_win_rate = win_rates.idxmax()
    worst_win_rate = win_rates.idxmin()
    print(f"\n✅ ANSWER: {best_win_rate.capitalize()} difficulty has the highest win rate ({win_rates[best_win_rate]}%)")
    print(f"   {worst_win_rate.capitalize()} difficulty has the lowest win rate ({win_rates[worst_win_rate]}%)")
    print("   Justification: Calculated as (wins / total games) × 100 for each difficulty level.")
    
    # ============================================
    # CREATE GRAPH: Average Score by Difficulty
    # ============================================
    print("\n" + "=" * 50)
    print("GRAPH: Average Score by Difficulty")
    print("=" * 50)
    
    plt.figure(figsize=(8, 6))
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    bars = plt.bar(avg_score_by_difficulty.index, avg_score_by_difficulty.values, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar, score in zip(bars, avg_score_by_difficulty.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                 f'{score}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Average Score by Difficulty Level', fontsize=16, fontweight='bold')
    plt.xlabel('Difficulty', fontsize=12)
    plt.ylabel('Average Score (points)', fontsize=12)
    plt.ylim(0, max(avg_score_by_difficulty.values) + 15)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Save the graph
    plt.savefig('score_by_difficulty.png', dpi=150, bbox_inches='tight')
    print("\n✅ Graph saved as 'score_by_difficulty.png'")
    plt.show()
    
    # ============================================
    # CREATE SECOND GRAPH: Win Rate by Difficulty
    # ============================================
    print("\n" + "=" * 50)
    print("GRAPH: Win Rate by Difficulty")
    print("=" * 50)
    
    plt.figure(figsize=(8, 6))
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    bars = plt.bar(win_rates.index, win_rates.values, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar, rate in zip(bars, win_rates.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{rate}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Win Rate by Difficulty Level', fontsize=16, fontweight='bold')
    plt.xlabel('Difficulty', fontsize=12)
    plt.ylabel('Win Rate (%)', fontsize=12)
    plt.ylim(0, 110)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Save the graph
    plt.savefig('win_rate_by_difficulty.png', dpi=150, bbox_inches='tight')
    print("\n✅ Graph saved as 'win_rate_by_difficulty.png'")
    plt.show()
    
    # ============================================
    # ADDITIONAL INSIGHTS
    # ============================================
    print("\n" + "=" * 50)
    print("ADDITIONAL INSIGHTS")
    print("=" * 50)
    
    # Average attempts by difficulty
    avg_attempts = df[df['Won'] == 'Yes'].groupby('Difficulty')['Attempts'].mean().round(1)
    print("\nAverage Attempts to Win (by difficulty):")
    for diff, attempts in avg_attempts.items():
        print(f"  {diff}: {attempts} attempts")
    
    # Total games played
    games_by_difficulty = df['Difficulty'].value_counts()
    print("\nGames Played by Difficulty:")
    for diff, count in games_by_difficulty.items():
        print(f"  {diff}: {count} games")
    
    # ============================================
    # SUMMARY
    # ============================================
    print("\n" + "=" * 60)
    print("📊 ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"✅ Total Games Analyzed: {len(df)}")
    print(f"✅ Total Wins: {(df['Won'] == 'Yes').sum()}")
    print(f"✅ Overall Win Rate: {(df['Won'] == 'Yes').sum() / len(df) * 100:.1f}%")
    print(f"✅ Overall Average Score: {df['Score'].mean():.1f}")
    print(f"✅ Best Difficulty (Score): {best_difficulty} ({best_score} points)")
    print(f"✅ Best Difficulty (Win Rate): {best_win_rate} ({win_rates[best_win_rate]}%)")
    
    print("\n📁 Output Files:")
    print("   - game_sessions.csv (dataset)")
    print("   - score_by_difficulty.png (bar chart)")
    print("   - win_rate_by_difficulty.png (bar chart)")
    
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)
    
    return df, avg_score_by_difficulty, win_rates


if __name__ == "__main__":
    analyze_game_data()
