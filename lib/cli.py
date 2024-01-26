# lib/cli.py
from rich.console import Console
console = Console()
from seed import seed_database, reseed_database, clear_data

from helpers import (
    exit_program,
    add_member,
    change_membership, 
    view_members,
    view_all_programs,
    add_program,
    delete_member, 
    delete_program,
    add_trainer,
    delete_trainer,
    view_all_locations,
    view_all_trainers,
    add_scheduled_program,
    add_location,
    view_schedule,
    delete_location,
    view_schedule,
    update_location_city,
    get_all_programs_by_trainer
)

def monkey():
    console.print("____________________________________", style="bold green")
    console.print("       VVVV               VVVV        ")
    console.print("       (__)               (__)")
    console.print("        \ \               / /")
    console.print("         \ \   \\|||//    / /")
    console.print("          > \   _   _   / <")
    console.print("           > \ / \ / \ / <", style="bold green")
    console.print("             > \\_o_o_// <")
    console.print("             > ( (_) ) <", style="bold green")
    console.print("              >|     |<")
    console.print("             / |\___/| \ ", style="bold green")
    console.print("             / (_____) \ ")
    console.print("             /         \ ")
    console.print("              /   o   \ ", style="bold green")
    console.print("               ) ___ (   ")
    console.print("              / /   \ \  ", style="bold green")
    console.print("             ( /     \ )")
    console.print("             ><       ><")
    console.print("            ///\     /\\\\", style="bold green")
    console.print("            '''       '''", style="bold green")


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            member_main()
        elif choice == "2":
            trainer_main()
        elif choice == "3":
            location_main()
        elif choice == "4":
            program_main()
        elif choice == "5":
            schedule_main()
        elif choice == "6":
            dev_main()
        else:
            print("Invalid choice")


def menu():
    monkey()
    
    console.print("Welcome to JKH Gym", style="bold blue")
    console.print("Please Select an Option:", style="bold")
    console.print("0. Exit the Program")
    console.print("1. View The Member Menu")
    console.print("2. View The Trainer Menu")
    console.print("3. View The Location Menu")
    console.print("4. View The Program Menu")
    console.print("5. View The Schedule Menu")
    console.print("6. Access Dev Menu")

def member_main():
    while True:
        member_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            view_members()
        elif choice == "3":
            add_member()
        elif choice == "4":
            change_membership()
        elif choice == "5":
            delete_member()

def member_menu():
    monkey()
    
    console.print("Here is The Member Menu", style="bold blue")
    console.print("Please Select an Option:", style="bold")
    console.print("0. Exit The Program")
    console.print("1. Go Back to The Main Menu")
    console.print("2. View All Members")
    console.print("3. Add a Member")
    console.print("4. Change a Member's Plan")
    console.print("5. Delete a Member")

def trainer_main():
    while True:
        trainer_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            view_all_trainers()
        elif choice == "3":
            add_trainer()
        elif choice == "4":
            delete_trainer()
        elif choice == "5":
            get_all_programs_by_trainer()

def trainer_menu():
    monkey()
    
    console.print("Here is The Trainer Menu", style="bold blue")
    console.print("Please Select an Option:", style="bold")
    console.print("0. Exit The Program")
    console.print("1. Go Back to The Main Menu")
    console.print("2. View All Trainers")
    console.print("3. Add a Trainer")
    console.print("4. Delete a Trainer")
    console.print("5. Lookup a Trainer's programs")

def location_main():
    while True:
        location_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            view_all_locations()
        elif choice == "3":
            add_location()
        elif choice == "4":
            update_location_city()
        elif choice == "5":
            delete_location()

def location_menu():
    monkey()

    console.print("0. Exit The Program")
    console.print("1. Go Back to The Main Menu")
    console.print("2. View All Locations")
    console.print("3. Add a Location")
    console.print("4. Update a Location")
    console.print("5. Delete a Location")

def program_main():
    while True:
        program_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            view_all_programs()
        elif choice == "3":
            add_program()
        elif choice == "4":
            delete_program()

def program_menu():
    monkey()

    console.print("0. Exit The Program")
    console.print("1. Go Back to The Main Menu")
    console.print("2. View All Programs")
    console.print("3. Add a Program")
    console.print("4. Delete a Program")

def schedule_main():
    while True:
        schedule_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            view_schedule()
        elif choice == "3":
            add_scheduled_program()

def schedule_menu():
    monkey()

    console.print("0. Exit The Program")
    console.print("1. Go Back to The Main Menu")
    console.print("2. View Schedule")
    console.print("3. Schedule a Program")

def dev_main():
    while True:
        dev_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            main()
        elif choice == "2":
            seed_database()
        elif choice == "3":
            reseed_database()
        elif choice == "4":
            clear_data()

def dev_menu():
    console.print("0. Exit The Program")
    console.print("1. Go Back to The Main Menu")
    console.print("2. Put in Test Data")
    console.print("3. Reset with Test Data")
    console.print("4. Clear All Data")

print("Thank you for using JKH Gym.")

if __name__ == "__main__":
    main()
