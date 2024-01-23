import sqlite3 

CONN = sqlite3.connect('lib/gym.db')
CURSOR = CONN.cursor()

class Member:
    def __init__(self, id, first_name, last_name, membership_type="Basic"):
        self.id = id
        self.first_name = first_name # Needs to be property
        self.last_name = last_name
        self.membership_type = membership_type # Needs to be property
        # self.classes_attended = [] 

    def upgrade_membership(self):
        if self.membership_type == "Basic":
            self.membership_type = "Premium"
            print(f"{self.name}'s membership upgraded to Premium.")

    def attend_class(self, exercise):
        self.classes_attended.append(exercise)
        print(f"{self.name} attended {exercise.name} class.")

    def display_info(self):
        membership_info = f"Membership Type: {self.membership_type}"
        classes_info = f"Classes Attended: {', '.join([exercise.name for exercise in self.classes_attended])}"

        print(f"Member Name: {self.name}\n{membership_info}\n{classes_info}")

    @classmethod 
    def create_member_table(cls):
        query = """
            CREATE TABLE IF NOT EXISTS `member_table` (
            id INTEGER PRIMARY KEY, 
            first_name TEXT, 
            last_name TEXT, 
            membership_type TEXT);
        """
        CURSOR.execute(query)
        CONN.commit()

    # @classmethod 
    # def drop_table(cls):
    #     query = """
    #         DROP TABLE IF EXISTS `member_table`;
    #     """
    #     CURSOR.execute(query)
    #     CONN.commit()

    def save(self):
        query = """
            INSERT INTO `member_table` ( `first_name`, `last_name`, `membership_type` )
            VALUES (?, ?, ?)
        """
        CURSOR.execute(query, (self.first_name, self.last_name, self.membership_type))
        CONN.commit()
        self.id = CURSOR.lastrowid 

    @classmethod 
    def create_member_row(cls, first_name, last_name, membership_type):
        member = cls(first_name, last_name, membership_type)
        member.save()
        return member 
    
    @classmethod 
    def new_member_db(cls, row):
        member = cls (
                id = row[0],
                first_name = row[1],
                last_name = row[2],
                membership_type = row[3]
            )
        print(member.first_name, member.last_name, member.membership_type)
        return member
    
    @classmethod 
    def get_all_members(cls):
        sql = """
            SELECT * FROM member_table
        """
        return [cls.new_member_db(one_row) for one_row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_name(cls, first_name, last_name):
        sql = """
            SELECT * FROM member_table
            WHERE first_name = ? 
            AND last_name = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (first_name, last_name)).fetchone()
        if not row:
            return None
        return Member(
            first_name = row[1],
            last_name = row[2],
            id = row[0]
        )

# Members
basic_member = Member("Jeffery")
premium_member = Member("Katie", membership_type="Premium")
