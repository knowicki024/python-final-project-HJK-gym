# lib/helpers.py
from models.location import Location
from models.member import Member
from models.program import Program
from models.trainer import Trainer
from models.schedule import Schedule

def exit_program():
    print("Goodbye!")
    exit()

def add_member():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    membership_type = input("Do you want Basic or Premium membership?: ")
    new_member = Member.create_member_row(first_name, last_name, membership_type)
    print(f'Member {new_member.id} {new_member.first_name} {new_member.last_name} has been added with the {new_member.membership_type} membership.')

    return new_member

def change_membership():
    member_id = input("Enter the member's ID: ")
    first_name = input("Enter the member's first name: ")
    last_name = input("Enter the member's last name: ")

    try:
        member_id = int(member_id)
    except ValueError:
        print("Invalid ID format. Please enter a numerical ID.")
        return

    member = Member.find_by_id(member_id)
    if not member:
        print("Member not found")
        return

    if member.first_name == first_name and member.last_name == last_name:
        new_membership_type = input(f"Current membership: {member.membership_type}.  Enter new membership type (Basic/Premium): ")
        if new_membership_type not in ["Basic", "Premium"]:
            print("Invalid membership type")
            return
        elif member.membership_type == new_membership_type:
            print(f"{member.first_name} already has a {new_membership_type} membership.")
            return
        member.membership_type = new_membership_type
        member.save()
        print(f"{member.first_name} {member.last_name}'s membership has been changed to {new_membership_type}.")
    else:
        print("Member details do not match.")


def view_members():
    members = Member.get_all()
    for member in members:

        print(f"Member Info:\n    ID: {member.id}\n    Name: {member.first_name} {member.last_name}\n    Membership Type: {member.membership_type}\n")

def view_all_programs():
    programs = Program.get_all()
    for program in programs:
        location = Location.find_by_id(program.location_id)
        trainer = Trainer.find_by_id(program.trainer_id)
        print(f"Program Info:\n    ID: {program.id}\n    Exercise: {program.exercise_name}\n    Trainer: {trainer.first_name} {trainer.last_name}\n    Location: {location.city}\n    Membership Required: {program.membership_required}\n")


def add_program():
    exercise_name = input("Enter name of class/exercise: ")
    view_all_trainers()
    trainer_first_name = input("Enter trainer's first name: ")
    trainer_last_name = input("Enter trainer's last name: ")
    view_all_locations()
    location_name = input("Enter location: ")
    membership_required = input("Which membership level is required: Basic or Premium? ")

    trainer = Trainer.find_by_name(trainer_first_name, trainer_last_name)
    location = Location.find_by_name(location_name)

    if not trainer:
        print("No trainer registered by that name.")
    elif not location:
        print("This location does not exist.")
        return
    if membership_required not in ["Basic", "Premium"]:
        print("Invalid membership type.")
        return

    new_program = Program.create(location.id, trainer.id, exercise_name, membership_required)

    print(f"Program added: {exercise_name} at {location_name} with Trainer {trainer_first_name} {trainer_last_name}, Membership Required: {membership_required}")
    return new_program

def delete_member():
    method = input("Delete by ID(1) or Name(2)? Enter 1 or 2: ")

    if method == "1":
        member_id = input("Enter the member ID: ")
        try:
            member_id = int(member_id)
            member = Member.find_by_id(member_id)
            if member:
                member.delete()
                print(f"Member with ID {member_id} has been deleted.")
            else:
                print("Member not found.")
        except ValueError:
            print("Invalid ID format. Please enter a numerical ID.")

    elif method == "2":
        first_name = input("Enter the member's first name: ")
        last_name = input("Enter the member's last name: ")
        member = Member.find_by_name(first_name, last_name)
        if member:
            member.delete()
            print(f"Member {first_name} {last_name} has been deleted.")
        else:
            print("Member not found or details do not match.")

def delete_program():
    program_id = input("Enter program ID to delete: ")
    program = Program.find_by_id(program_id)
    if not program:
        print("Program not found.")
        return 
    program.delete()
    print(f"Program {program.exercise_name} has been deleted.")

def add_trainer():
    first_name = input("Enter trainer's first name: ")
    last_name = input("Enter trainer's last name: ")
    new_trainer = Trainer.create(first_name, last_name)
    print(f'Trainer {new_trainer.id} {new_trainer.first_name} {new_trainer.last_name} has been added.')

    return new_trainer

def delete_trainer():
    first_name = input("Enter trainers first name: ")
    last_name = input("Enter trainers last name: ")
    if trainer := Trainer.find_by_name(first_name, last_name):
        trainer.delete()
        print(f"Trainer {first_name} has been deleted.")
    else:
        print("Trainer not found.")

def add_location():
    city = input("Enter the city for the new location: ")

    try:
        new_location = Location.create(city)
        print(f'New location added: {new_location.city} with ID {new_location.id}')
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_location():
    method = input("Delete by ID(1) or City Name(2)? Enter 1 or 2: ")

    if method == "1":
        location_id = input("Enter the location ID: ")
        try:
            location_id = int(location_id)
            location = Location.find_by_id(location_id)
            if location:
                location.delete()
                print(f"Location with ID {location_id} has been deleted.")
            else:
                print("Location not found.")
        except ValueError:
            print("Invalid ID format. Please enter a numerical ID.")

    elif method == "2":
        city = input("Enter the location's city name: ")
        location = Location.find_by_name(city)
        if location:
            location.delete()
            print(f"Location in {city} has been deleted.")
        else:
            print("Location not found or city name does not match.")

    else:
        print("Invalid option selected.")
    
def update_location_city():
    location_id = input("Enter the JKH Gym ID of the location you want to update: ")

    try:
        location_id = int(location_id)
    except ValueError:
        print("Invalid ID format.")
        return

    location = Location.find_by_id(location_id)
    if not location:
        print(f"No JKH Gym found with ID: {location_id}")
        return

    print(f"Current city for JKH Gym with ID {location_id} is '{location.city}'.")
    new_city = input("Enter the new city name: ")

    try:
        location.city = new_city
        location.update()
        print(f"JKH Gym ID {location_id} has been updated to city: {new_city}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_locations():
    locations = Location.get_all_locations()
    for location in locations:
        print(f"Location Info:\n    ID: {location.id}\n    City: {location.city}\n")

def view_all_trainers():
    trainers = Trainer.get_all()
    for trainer in trainers:
        print(f"Trainer Info:\n    ID: {trainer.id}\n    Name: {trainer.first_name} {trainer.last_name}\n")

def add_scheduled_program():
    view_all_programs()
    program_id = input("Enter program ID for program you want to schedule: ")
    program = Program.find_by_id(program_id)

    trainer = Trainer.find_by_id(program.trainer_id)
    location = Location.find_by_id(program.location_id)

    view_members()
    member_id = input("Enter member ID for who would like to attend: ")
    member = Member.find_by_id(member_id)
    if program.membership_required == "Premium" and member.membership_type != "Premium":
        print("Sorry! Member needs to be premium member to attend.")
    else:
        room = input("Enter the room name/number this will be held in: ")
        date = input("Enter the date you want this scheduled on (MMDDYY): ")
        start_time = input("Enter the time this program will start (24hr): ")
        end_time = input("Enter the time this program will end (24hr): ")
        new_schedule = Schedule.create(program.id, member.id, room, date, start_time, end_time)

        print(f"""{member.first_name} {member.last_name} is set to attend {program.exercise_name} on {new_schedule.date} from {new_schedule.start_time} to {new_schedule.end_time}.  Will take place in room {new_schedule.room} at the {location.city} location.  {trainer.first_name} {trainer.last_name} will be leading this one!""")

        return new_schedule

def view_schedule():
    schedules = Schedule.get_all()
    for schedule in schedules:
        program = Program.find_by_id(schedule.program_id)
        member = Member.find_by_id(schedule.member_id)
        print(f"""Schedule Info:\n        ID: {schedule.id}\n        Program Name: {program.exercise_name}
        Member Name: {member.first_name} {member.last_name}\n        Room: {schedule.room}\n        Date: {schedule.date}\n        Start Time: {schedule.start_time}\n        End Time: {schedule.end_time}\n""")