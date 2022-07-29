# Write your code here!
class Member: 
    def __init__(self, name):
        self.full_name = name
    
    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')


class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason


class Instructor(Member):
    def __init__(self, name, bio):
        super().__init__(name)
        self.bio = bio
        self.skillset = []

    def add_skill(self, skill):
        self.skillset.append(skill)


class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
    
    def add_participant(self, participant):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)

    def print_details(self):
        print(f'Workshop - {self.date} - {self.subject}\n')
        print('\nStudents:')
        for index, s in enumerate(self.students, 1):
            print(f'{index}. {s.full_name} - {s.reason}')

        print('\nInstructors:')
        for index, i in enumerate(self.instructors, 1):
            print(f'{index}. {i.full_name} - ', end="")
            for skill in i.skillset:
                if skill != i.skillset[-1]:
                    print(f'{skill}', end=", ")
                else:
                    print(f'{skill}')

            print(f"\t{i.bio}")





def main():
    workshop = Workshop("12/03/2014", "Shutl")

    jane = Student("Jane Doe", "I am trying to learn programming and need some help")
    lena = Student("Lena Smith", "I am really excited about learning to program!")
    vicky = Instructor("Vicky Python_Basic", "I want to help people learn coding.")
    vicky.add_skill("HTML")
    vicky.add_skill("JavaScript")
    nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python_Basic and want to spread the love")
    nicole.add_skill("Python_Basic")

    workshop.add_participant(jane)
    workshop.add_participant(lena)
    workshop.add_participant(vicky)
    workshop.add_participant(nicole)
    workshop.print_details()

if __name__ == "__main__":
    main()