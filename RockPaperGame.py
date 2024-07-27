import random

def game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == '4':
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {choices[int(user_choice) - 1].capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == '1':
            if computer_choice == 'rock':
                print("It's a tie!")
            elif computer_choice == 'paper':
                print("Paper covers rock. Computer wins!")
                computer_score += 1
            else:
                print("Rock smashes scissors. You win!")
                user_score += 1
        elif user_choice == '2':
            if computer_choice == 'rock':
                print("Paper covers rock. You win!")
                user_score += 1
            elif computer_choice == 'paper':
                print("It's a tie!")
            else:
                print("Scissors cuts paper. Computer wins!")
                computer_score += 1
        else:
            if computer_choice == 'rock':
                print("Rock smashes scissors. Computer wins!")
                computer_score += 1
            elif computer_choice == 'paper':
                print("Scissors cuts paper. You win!")
                user_score += 1
            else:
                print("It's a tie!")

        print(f"Score - You: {user_score}, Computer: {computer_score}")

game()