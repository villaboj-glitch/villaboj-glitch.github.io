# Josue VillaBonilla
# 13 MAY 2026
# Final Project
# This program is a beginner-level pet rescue game where NULL looks for his cat Drizzy inside a small cubicle office.


import random
import time


def pause():
    time.sleep(1)


def show_intro():
    print("==========================================")
    print("       🐈 NULL'S OFFICE PET RESCUE 🕵️ 🔍  ")
    print("==========================================")
    print("NULL stayed late at work and noticed his cat Drizzy is missing.")
    print("Drizzy is somewhere inside the small cubicle office.🐈")
    print("Search the office, find clues, and rescue Drizzy before NULL gets too tired.")
    print()


def show_status(player):
    print("\n---------- STATUS ----------")
    print("Name:", player["name"])
    print("Location:", player["location"])
    print("Energy:", player["energy"])
    print("Clues Found:", player["clue_count"])
    print("Mood:", player["mood"])
    print("Inventory:", player["inventory"])
    print("----------------------------")


def show_menu():
    print("\nWhat should NULL do?⏳")
    print("1. Search the cubicles📄")
    print("2. Check the break room🚪")
    print("3. Look near the printer🖨️")
    print("4. Check the server room💻")
    print("5. Try the supply closet🏢")
    print("6. Quit game")


def add_item(player, item):
    if item not in player["inventory"]:
        player["inventory"].append(item)
        print("You added", item, "to your inventory.")


def add_clue(player, clue):
    if clue not in player["clues"]:
        player["clues"].append(clue)
        player["clue_count"] = player["clue_count"] + 1
        player["mood"] = "hopeful"
        print("New clue found:", clue)
    else:
        print("You already found this clue.❓")


def search_cubicles(player):
    player["location"] = "Cubicles"
    player["moves"] = player["moves"] + 1
    player["energy"] = player["energy"] - 1

    print("\nNULL checks under desks and between cubicle walls...")
    pause()

    clues = [
        "orange cat hair on a keyboard",
        "tiny paw prints near a rolling chair🐾!!",
        "a sticky note knocked onto the floor💡"
    ]

    clue = random.choice(clues)
    add_clue(player, clue)


def check_break_room(player):
    player["location"] = "Break Room"
    player["moves"] = player["moves"] + 1

    print("\nNULL walks into the break room...🔍")
    pause()

    event = random.choice(["snack", "noise", "empty"])

    if event == "snack":
        print("NULL finds a tuna snack on the counter!!🦴")
        add_item(player, "tuna snack")
        player["energy"] = player["energy"] + 2
        player["mood"] = "focused"
        print("NULL gains 2 energy.")

    elif event == "noise":
        print("NULL hears a tiny meow coming from the hallway!!🐈‍⬛")
        add_clue(player, "a small meow near the supply closet")
        player["energy"] = player["energy"] - 1

    else:
        print("The break room is quiet, but NULL takes a quick rest.😴")
        player["energy"] = player["energy"] + 1
        player["mood"] = "calm"


def check_printer(player):
    player["location"] = "Printer Area"
    player["moves"] = player["moves"] + 1
    player["energy"] = player["energy"] - 1

    print("\nNULL checks around the printer area...")
    pause()

    event = random.choice(["toy", "paper", "nothing"])

    if event == "toy":
        print("NULL finds Drizzy's toy mouse 🐭 behind the printer.")
        add_item(player, "toy mouse")
        add_clue(player, "Drizzy's toy was near the printer")

    elif event == "paper":
        print("A paper is stuck in the printer with little paw marks on it.📄")
        add_clue(player, "paw marks on printer paper🐾")

    else:
        print("NULL only finds old print jobs. No new clue here =/.")
        player["mood"] = "confused"


def check_server_room(player):
    player["location"] = "Server Room"
    player["moves"] = player["moves"] + 1
    player["energy"] = player["energy"] - 2

    print("\nNULL carefully opens the server room door...🕵️")
    pause()

    if "office badge" not in player["inventory"]:
        print("NULL finds an office badge on the floor.")
        add_item(player, "office badge")
        add_clue(player, "the badge was near the server room")
    else:
        print("The servers are humming, and NULL hears a soft scratch in the wall.")
        add_clue(player, "scratching sound near the supply closet")


def try_supply_closet(player):
    player["location"] = "Supply Closet"
    player["moves"] = player["moves"] + 1
    player["energy"] = player["energy"] - 1

    print("\nNULL walks up to the supply closet...🕵️")
    pause()

    if player["clue_count"] >= 3 and "office badge" in player["inventory"]:
        print("NULL uses the office badge and follows the clues.🕵️")
        pause()

        if "tuna snack" in player["inventory"]:
            print("NULL opens the tuna snack and softly calls Drizzy's name.")
            print("Drizzy pops out from behind a box of printer paper!🐱🖨️")
            player["found_drizzy"] = True
            player["mood"] = "happy"

        else:
            chance = random.randint(1, 2)

            if chance == 1:
                print("NULL slowly opens the closet door.")
                print("Drizzy is curled up inside a box!")
                player["found_drizzy"] = True
                player["mood"] = "happy"
            else:
                print("NULL hears Drizzy, but Drizzy is hiding too well.😴")
                print("Maybe a snack would help next time.")
                player["mood"] = "worried"

    else:
        print("The supply closet is locked or NULL does not have enough clues yet.⚠️")
        print("Hint: Find at least 3 clues and the office badge.")
        player["mood"] = "determined"


def ending_win(player):
    print("\n====================================")
    print("         ⭐ 🎉 YOU WIN! 🐈🐈")
    print("======================================")
    print("NULL found Drizzy 🐈 and carried him safely out of the office.")
    print("Drizzy is happy, and NULL can finally go home.❤️")
    print("Total moves:", player["moves"])
   


def ending_tired(player):
    print("\n====================================")
    print("          ⚠️  GAME OVER  ⚠️ ")
    print("======================================")
    print("NULL got too tired to keep searching.😴")
    print("Drizzy is still hiding somewhere in the office.")
    print("Try again and manage your energy better.📌")


def main():
    player = {
        "name": "NULL",
        "cat_name": "Drizzy",
        "location": "Office Entrance",
        "energy": 10,
        "mood": "worried",
        "inventory": [],
        "clues": [],
        "clue_count": 0,
        "moves": 0,
        "found_drizzy": False
    }

    show_intro()

    while player["energy"] > 0 and player["found_drizzy"] == False:
        show_status(player)
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            search_cubicles(player)

        elif choice == "2":
            check_break_room(player)

        elif choice == "3":
            check_printer(player)

        elif choice == "4":
            check_server_room(player)

        elif choice == "5":
            try_supply_closet(player)

        elif choice == "6":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    if player["found_drizzy"] == True:
        ending_win(player)

    elif player["energy"] <= 0:
        ending_tired(player)


main()