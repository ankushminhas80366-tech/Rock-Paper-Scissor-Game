import random
def game():

    wants=input("Do you want to play the game? (yes/no): ")
    if wants.lower()=="yes":
        print("Great! Let's start the game.")
    else:
        print("Okay, maybe next time!")
        return
    
    print("Welcome to the Rock,Paper,Scissors game!")
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


if __name__=="__main__":
    game()   