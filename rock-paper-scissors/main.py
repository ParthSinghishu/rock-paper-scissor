from game_module import play_round, get_user_choice, show_scoreboard

def main():
    print("=== Rock Paper Scissors ===")
    print("First to reach the required wins wins the match.")

    # choose best of N rounds (odd)
    while True:
        try:
            n = int(input("Enter number of rounds (odd number, e.g., 3 or 5): ").strip())
            if n % 2 == 0 or n <= 0:
                print("Please enter a positive odd number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    required_wins = n // 2 + 1
    user_score = 0
    cpu_score = 0
    round_no = 1

    while user_score < required_wins and cpu_score < required_wins:
        print(f"\n--- Round {round_no} ---")
        user_choice = get_user_choice()
        cpu_choice, result = play_round(user_choice)

        if result == "win":
            user_score += 1
            print("You win this round!")
        elif result == "lose":
            cpu_score += 1
            print("CPU wins this round!")
        else:
            print("This round is a draw!")

        show_scoreboard(user_score, cpu_score)
        round_no += 1

    if user_score > cpu_score:
        print("\nCONGRATULATIONS! You won the match.")
    else:
        print("\nCPU won the match. Better luck next time.")

    save = input("\nDo you want to save the match summary to a file? (y/n): ").strip().lower()
    if save == "y":
        from report_module import save_match_report
        save_match_report(user_score, cpu_score, n)
        print("Match summary saved in reports/ folder.")

if __name__ == '__main__':
    main()
