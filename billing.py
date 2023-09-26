# ----------------------------------------------------------------
# Authors: Kurt Brown 
# Date: July 11, 2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
from datetime import date, time, datetime
def display_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------

    # Set the number of hours to 0 to start
    num_hours = 0
    # If the student is an in state student, charge them $225 per credit
    # Set the if statement equal to True
    # If they are out of state, charge them $850 per credit
    if s_in_state[id] == True:
        tuition = 225
        student_status = "In-State"
    else:
        tuition = 850
        student_status = "Out-of-State"

    # For each class in the roster
    # Check if the student id is there
    # If it is, add it to the number of hours
    # Multiple the cost of the tuition by the number of hours
    print(f'Tuition Summary')
    print(f'Student: {id}, {student_status} Student')
    dt = datetime.now()
    print(f'Generated on {dt.strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'Course\t\t\tHours\t\t  Cost')
    print(f'------\t\t\t-----\t\t--------')


    for wt_course in c_rosters:
        if id in c_rosters[wt_course]:
            num_hours += c_hours[wt_course]
            each_course_cost = tuition * c_hours[wt_course]
            total_cost = num_hours * tuition
            total_hours = num_hours
            print(f'{wt_course} \t\t\t\t{c_hours[wt_course]} \t\t${each_course_cost:.2f}')

    print('\t\t\t--------- \t\t--------')
    print(f'Total \t\t\t\t{total_hours} \t\t${total_cost:.2f}\n')




