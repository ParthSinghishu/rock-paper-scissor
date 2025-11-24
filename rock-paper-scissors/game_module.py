import random

CHOICES = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors or r/p/s): ").strip().lower()
        if choice in ['r', 'rock']:
            return 'rock'
        if choice in ['p', 'paper']:
            return 'paper'
        if choice in ['s', 'scissors', 'scissor']:
            return 'scissors'
        print("Invalid choice. Please enter rock, paper, or scissors (or r/p/s).")

def cpu_choice_random():
    return random.choice(CHOICES)

def decide_winner(user, cpu):
    if user == cpu:
        return 'draw'

    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if wins[user] == cpu:
        return 'win'
    else:
        return 'lose'

def play_round(user_choice):
    cpu = cpu_choice_random()
    print(f'CPU chose: {cpu}')
    result = decide_winner(user_choice, cpu)
    return cpu, result

def show_scoreboard(user_score, cpu_score):
    print(f'Current Score -> You: {user_score} | CPU: {cpu_score}')
