import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to stop.")

    while True:
        user_choice = input("\nYour choice: ").lower()

        if user_choice == 'quit':
            print("\nGame Over!")
            print(f"Final Score - You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"📢 Result: {result}")

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"📊 Score - You: {user_score} | Computer: {computer_score}")

# Run the game
play_game()
