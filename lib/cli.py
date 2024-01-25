# lib/cli.py
from rich.console import Console
console = Console()

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
    delete_trainer
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_members()
        elif choice == "2":
            add_member()
        elif choice == "3":
            change_membership()
        elif choice == "4":
            delete_member()
        elif choise == "5":
            view_all_trainers() 
        elif choice == "6":
            add_trainer()
        elif choice == "7":
            update_trainer():
            pass
        elif choice == "8":
            delete_trainer()
        elif choice == "9":
            view_all_locations()
        elif choice == "10":
            add_location()
            pass
        elif choice == "11":
            update_location()
            pass
        elif choice == "12":
            delete_location()
            pass
        elif choice == "13":
            view_all_programs()
        elif choice == "14":
            add_program()
        elif choice == "15":
            update_program()
            pass
        elif choice == "16":
            delete_program()

        else:
            print("Invalid choice")


def menu():
    console.print("____________________________________", style="bold green")
    console.print("       VVVV               VVVV        ")
    console.print("       (__)               (__)")
    console.print("        \ \               / /")
    console.print("         \ \   \\|||//   / /")
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
    
    console.print("Welcome to JKH Gym", style="bold blue")
    console.print("Please select an option:", style="bold")
    console.print("0. Exit the program")
    console.print("1. View Members")
    console.print("2. Add New Member")
    console.print("3. Change Membership Plan")
    console.print("4. Delete Member")
    console.print("5. View Trainers")
    console.print("6. Add Trainer")
    console.print("7. Update Trainer")
    console.print("8. Delete Trainer")
    console.print("9. View Locations")
    console.print("10. Add Location")
    console.print("11. Update Location")
    console.print("12. Delete Location")
    console.print("13. View All Programs")
    console.print("14. Add New Exercise Program")
    console.print("15. Update Existing Exercise Program")
    console.print("16. Delete Exercise Program")

print("Thank you for using JKH Gym.")

if __name__ == "__main__":
    main()
