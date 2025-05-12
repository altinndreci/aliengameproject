#title screen, play or exit game
def title_screen():
    print("\n" + "="*60)
    print("             XenoBlood: Attack on Aliens")
    print("="*60)
    print("         A Text-Based Fighting Adventure Game")
    print("\n              [1] Play")
    print("              [0] Exit")
    print("="*60)

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            break
        elif choice == "0":
            print("\nThe world falls silent as you walk away...\n")
            print("Goodbye, brave human.")
            exit()
        else:
            print("Invalid input. Press 1 to Play or 0 to Exit.\n")
