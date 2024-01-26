#1/user/bin/env python3 

from models.__init__ import CONN, CURSOR 
from models.location import Location
from models.member import Member
from models.program import Program
from models.trainer import Trainer
from models.schedule import Schedule

def seed_database():

    # Create tables
    Location.create_table()
    Member.create_table()
    Program.create_table()
    Trainer.create_table()
    Schedule.create_table()


    # Create and save locations
    L1 = Location.create("Chicago")
    L2 = Location.create("Memphis")   
    L3 = Location.create("St. Louis")
    L4 = Location.create("Louisville")
    L5 = Location.create("Seatle")

    # Create and save members
    m1 = Member.create("Joe", "Thornton")
    m2 = Member.create("Conor", "Bedard")
    m3 = Member.create("Brenda", "Scott")
    m4 = Member.create("Kathy", "Washington")
    m5 = Member.create("Patrick", "Kane")

    # Create and save trainers
    t1 = Trainer.create("Bob", "Thornton") 
    t2 = Trainer.create("Tony", "Little")
    t3 = Trainer.create("Tracy", "Anderson")
    t4 = Trainer.create("Jillian", "Michales")
    t5 = Trainer.create("Bob", "Harper")
    t6 = Trainer.create("Kathy", "Smith")

    # Create and save programs
    p1 = Program.create(1, 1, "Zumba", "Premium")
    p2 = Program.create(2, 2, "Rowing", "Basic")
    p3 = Program.create(3,3, "Cardio", "Basic")
    p4 = Program.create(1, 2, "Strength", "Premium")

    s1 = Schedule.create(1, 2, "101", "012524", "0900", "1000")

def reseed_database():

    #Deleting tables to clear 
    Trainer.drop_table()
    Location.drop_table()
    Program.drop_table()
    Member.drop_table()
    Schedule.drop_table()

    # Create tables
    Location.create_table()
    Member.create_table()
    Program.create_table()
    Trainer.create_table()
    Schedule.create_table()


    # Create and save locations
    L1 = Location.create("Chicago")
    L2 = Location.create("Memphis")   
    L3 = Location.create("St. Louis")
    L4 = Location.create("Louisville")
    L5 = Location.create("Seatle")

    # Create and save members
    m1 = Member.create("Joe", "Thornton")
    m2 = Member.create("Conor", "Bedard")
    m3 = Member.create("Brenda", "Scott")
    m4 = Member.create("Kathy", "Washington")
    m5 = Member.create("Patrick", "Kane")

    # Create and save trainers
    t1 = Trainer.create("Bob", "Thornton") 
    t2 = Trainer.create("Tony", "Little")
    t3 = Trainer.create("Tracy", "Anderson")
    t4 = Trainer.create("Jillian", "Michales")
    t5 = Trainer.create("Bob", "Harper")
    t6 = Trainer.create("Kathy", "Smith")

    # Create and save programs
    p1 = Program.create(1, 1, "Zumba", "Premium")
    p2 = Program.create(2, 2, "Rowing", "Basic")
    p3 = Program.create(3,3, "Cardio", "Basic")
    p4 = Program.create(1, 2, "Strength", "Premium")

    s1 = Schedule.create(1, 2, "101", "012524", "0900", "1000")

def clear_data():
    #Deleting tables to clear 
    Trainer.drop_table()
    Location.drop_table()
    Program.drop_table()
    Member.drop_table()
    Schedule.drop_table()

    # Create tables
    Location.create_table()
    Member.create_table()
    Program.create_table()
    Trainer.create_table()
    Schedule.create_table()

if __name__ == "__main__":
    seed_database()
