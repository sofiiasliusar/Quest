import random

# List of fortunes
fortunes = [
    "You will find great success in the near future.",
    "A pleasant surprise awaits you today.",
    "Take a risk, it will pay off in the end.",
    "Good things come to those who wait.",
    "Be prepared for a life-changing opportunity.",
    "Your creativity will shine in the coming days.",
    "You will make new friends who will enrich your life.",
]

# Function to get a random fortune
def get_random_fortune():
    return random.choice(fortunes)

# Main program
print("Welcome to the Fortune Teller!")
while True:
    input("Press Enter to receive your fortune...")
    fortune = get_random_fortune()
    print("\nYour fortune is:")
    print(fortune)
    
    play_again = input("\nDo you want to try again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for visiting the Fortune Teller!")
        break