# ----------------------------------------------------------------
# Authors: Kurt Brown and Andrew Jacob
# Date: July 12, 2023
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------


student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
student_in_state = {'1001': True, '1002': False, '1003': True, '1004': False}

course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    # Variable named wt_course represents the course to add
    wt_course = input(f'Enter course you want to add: ')
    # First, if the course entered is not offered display an error
    # Remember, the courses are CSC101, CSC102, CSC103, CSC104
    if wt_course not in c_roster:
        print(f'Course not found\n')
    # Next, if the student is already registered.
    # Take the length of the courses (4) and compare it to the max size (4)
    # If they are equal, then the course is full
    elif len(c_roster[wt_course]) == c_max_size[wt_course]:
        print(f'Course already full.\n')
    # Go through the roster and check if the student id is in the roster dictionary
    #If true, then the student is already in the course
    elif id in c_roster[wt_course]:
        print(f'You are already enrolled in that course.\n')
    # The last option is if everything is okay, so we will add the id to the course roster.
    else:
        c_roster[wt_course].append(id)
        print("Course added\n")

def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------

    wt_course = input(f'Enter course you want to drop: ')
    # Go through the roster and see if the entered course is in the roster
    # Remember, the courses are CSC101, CSC102, CSC103, CSC104
    if wt_course not in c_roster:
        print(f'Course not found\n')
    # Else, if the student is not enrolled in the course
    # We can check this by seeing if the student's ID is in the class roster
    elif id not in c_roster[wt_course]:
        print(f'You are not enrolled in that course.\n')
    # The only option left is if everything is okay. In that case, drop the course
    # Use the dictionary method remove() to do this.
    else:
        c_roster[wt_course].remove(id)
        print(f'Course dropped\n')

def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------
    # temporarily avoid empty function definition

    print(f'Courses registered: ')
    # Variable to hold the total number of courses
    number_of_courses = 0

    # For the entered course that are in the roster
    # Check to see if the student id is in the roster dictionary
    # If it is, increase the count of number of courses by 1
    # Print all of the courses, and then print the number of courses
    for wt_course in c_roster:
        if id in c_roster[wt_course]:
            number_of_courses += 1
            print(wt_course)
    print(f'Total number: {number_of_courses}\n')