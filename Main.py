import random

def manual():

    time=int(input("Enter how many time you want to play for: "))
    user1_points=0
    user2_points=0
    current_play=1
    choices=["rock","paper","scissors"]

    while time > 0:
        print(f"\n--- Play {current_play} ---") 
        user1=input("Player 1 enter your choice (rock, paper, scissors): ").lower()
        user2=input("Player 2 enter your choice (rock, paper, scissors): ").lower()
        if user1 not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return
        if user2 not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return
        print(f"Player 1 choice: {user1}")
        print(f"Player 2 choice: {user2}")
        if user1==user2:
            print("It's a tie!")
            time-=1
            current_play+=1
        elif (user1=="rock" and user2=="scissors") or (user1=="paper" and user2=="rock") or (user1=="scissors" and user2=="paper"):
            print("Player 1 wins! 🎉")
            time-=1
            user1_points+=1
            current_play+=1
        else:
            print("Player 2 wins! 🎉")
            time-=1
            user2_points+=1
            current_play+=1
    print(f"Final Scores - Player 1: {(user1_points)}, Player 2: {(user2_points)}")
    if (user1_points) > (user2_points):
        print("Congratulations! Player 1 is the overall winner! 🏆")
    elif (user1_points) == (user2_points):
        print("It's a tie overall! 🤝")
    else:
        print("Player 2 is the overall winner! Better luck next time! 🤖")


def game():
    choices=["rock","paper","scissors"]
    time=int(input("Enter how many time you want to play for: "))
    user_points=0
    computer_points=0
    current_play=1
    while time > 0:
        print(f"\n--- Play {current_play} ---") 
        user=input("Enter your choice (rock, paper, scissors): ").lower()
        if user not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return
        computer=random.choice(choices)
        print(f"Your choice: {user}")
        print(f"🤖Computer choose: {computer}")

        if user==computer:
            print("It's a tie!")
            time-=1
            current_play+=1
        elif (user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
            print("You win! 🎉")
            time-=1
            user_points+=1
            current_play+=1
        else:
            print("Computer wins! 😢")
            print("You Lose! 😢")
            time-=1
            computer_points+=1
            current_play+=1

    print(f"Final Scores - You: {(user_points)}, Computer: {(computer_points)}")

    if (user_points) > (computer_points):
        print("Congratulations! You are the overall winner! 🏆")
    elif (user_points) == (computer_points):
        print("It's a tie overall! 🤝")
    else:
        print("Computer is the overall winner! Better luck next time! 🤖")

def main():
    wants=input("Do you want to play the Game? (yes/no): ")
    if wants.lower()=='yes':
        print("Great! Let's start the game.")
    else:
        print("Okay, maybe next time!")
        return
    option=input("Do you want to play against the computer or another player? (computer/player): ").lower()
    if option=="computer":
        game()
    elif option=="player":
        manual()
    else:
        print("Invalid option. Please choose 'computer' or 'player'.")

if __name__=="__main__":
    main()