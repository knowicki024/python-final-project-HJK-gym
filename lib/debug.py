#!/usr/bin/env python3
# lib/debug.py
import ipdb; 
from models.__init__ import CURSOR, CONN

from models.program import Program
from models.schedule import Schedule
from models.location import Location
from models.trainer import Trainer
from models.member import Member

print("In Debugger!")

Trainer.drop_table()
Location.drop_table()
Program.drop_table()
Member.drop_table()
Schedule.drop_table()

Trainer.create_table()
Location.create_table()
Program.create_table()
Member.create_table()
Schedule.create_table()

L1 = Location.create("Chicago")
L2 = Location.create("Memphis")   
L3 = Location.create("St. Louis")
L4 = Location.create("Louisville")
L5 = Location.create("Seatle")

t1 = Trainer.create("Bob", "Thornton") 
t2 = Trainer.create("Tony", "Little")
t3 = Trainer.create("Tracy", "Anderson")
t4 = Trainer.create("Jillian", "Michales")
t5 = Trainer.create("Bob", "Harper")
t6 = Trainer.create("Kathy", "Smith")

p1 = Program.create(1, 1, "Zumba", "Premium")
p2 = Program.create(2, 2, "Rowing", "Basic")
p3 = Program.create(3,3, "Cardio", "Basic")
p4 = Program.create(1, 2, "Strength", "Premium")

m1 = Member.create("Joe", "Thornton")
m2 = Member.create("Conor", "Bedard")
m3 = Member.create("Brenda", "Scott")
m4 = Member.create("Kathy", "Washington")
m5 = Member.create("Patrick", "Kane")

s1 = Schedule.create(1, 2, "101", "012524", "0900", "1000")


ipdb.set_trace()