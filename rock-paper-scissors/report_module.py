import os
from datetime import datetime

def save_match_report(user_score, cpu_score, rounds):
    os.makedirs('reports', exist_ok=True)
    filename = datetime.now().strftime('reports/match_%Y%m%d_%H%M%S.txt')

    with open(filename, 'w') as f:
        f.write('Rock Paper Scissors - Match Summary\n')
        f.write(f'Total rounds (best of): {rounds}\n')
        f.write(f'User score: {user_score}\n')
        f.write(f'CPU score: {cpu_score}\n')

        if user_score > cpu_score:
            f.write('Result: User won the match\n')
        elif cpu_score > user_score:
            f.write('Result: CPU won the match\n')
        else:
            f.write('Result: Draw\n')

    return filename
