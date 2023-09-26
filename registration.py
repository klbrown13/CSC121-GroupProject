# ----------------------------------------------------------------
# Authors: Kurt Brown
# Date: July 12, 2023
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import student
import billing

def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}


    while True:
        id = input('Enter ID to log in, or 0 to quit: ')
        if id == '0':
            break
        else:
            if login(id, student_list):
                response = ''

                while response != '0':
                    print('Enter 1 to add course, 2 to drop course,')
                    response = input('3 to list courses, 4 to show bill, 0 to exit: ')
                    if response == '1':
                        student.add_course(id, course_roster, course_max_size)
                    elif response == '2':
                        student.drop_course(id, course_roster)
                    elif response == '3':
                        student.list_courses(id, course_roster)
                    elif response == '4':
                        billing.display_bill(id, student_in_state, course_roster, course_hours)
                    elif response == '0':
                        print('Session ended.\n')
                    else:
                        print('Input is not a valid response.\n')
    print('')

def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    # Variable named pin number - students must enter a pin number
    pin_number = input("Enter PIN: ")

    # Checks if the entered pin number is in the student_list dictionary
    if (id, pin_number) in s_list:
        print(f'ID and PIN verified\n')
        return True
    else:
        print(f'ID or PIN incorrect\n')
        return False

main()
