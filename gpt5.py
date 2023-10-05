import random

def shoot_penalty():
    print("You are taking a penalty kick!")
    player_choice = input("Choose a direction (left, center, right): ").lower()
    goalkeeper_choice = random.choice(["left", "center", "right"])

    print(f"You aimed {player_choice}, and the goalkeeper dived {goalkeeper_choice}.")
    
    if player_choice == goalkeeper_choice:
        print("The goalkeeper saved your penalty!")
        return False
    else:
        print("You scored a goal!")
        return True

def main():
    player_score = 0
    computer_score = 0
    
    print("Welcome to Penalty Shootout Game!")

    while True:
        print(f"Score: You {player_score} - {computer_score} Computer")

        # Take a penalty
        if shoot_penalty():
            player_score += 1
        else:
            computer_score += 1

        # Ask if the player wants to continue
        play_again = input("Do you want to take another penalty? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Game Over!")
    print(f"Final Score: You {player_score} - {computer_score} Computer")

if __name__ == "__main__":
    main()
