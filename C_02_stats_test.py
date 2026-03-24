if rounds_played > 0:
    # calculate stats
    rounds_won = rounds_played - user_wrong
    percent_won = user_right / rounds_played * 100
    percent_lost = user_wrong / rounds_played * 100

    # Output Game Stats
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"😎 Won: {percent_won:.2f} \t "
          f"😭 Lost: {percent_lost:.2f} \t ")

    # ask user if they want to see game history
    see_history = yes_no("Do you want to see the game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)
            print()

    print("Thanks for playing!")