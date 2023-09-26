# CSC121-GroupProject
Group Project for the CSC121 Python class

PROJECT DESCRIPTION

You have learned quite a lot about the basics of Python programming.  In this project, you will integrate what you have learned to develop a larger program.

This program creates a class registration system.  Students log into the class registration system and then they can add courses, drop courses, and list the courses for which they have registered.

This program has 6 functions in 3 modules: a student module, a billing module, and a main module.
 
Module: student.py
You must define the following functions in the student module.
Function	Specification
add_course(id, c_roster, c_max_size)	This function adds a student to a course.  It has three parameters: 
•	id is the ID of the student to be added
•	c_roster is a dictionary of courses offered with their student rosters
•	c_max_size is a dictionary of maximum class sizes  
This function asks user to enter the course they want to add.  
•	If the course is not offered, display error message and return.  
•	If student already registered for the course, display error message and return. 
•	If the course is full, display error message and return. 
•	If all error conditions are avoided, add the student ID to the course’s roster and display a message.  
This function has no return value.  
drop_course(id, c_roster)	This function drops a student from a course.  It has two parameters: 
•	id is the ID of the student to be dropped 
•	c_roster is a dictionary of courses offered with their student rosters
This function asks user to enter the course they want to drop.  
•	If the course is not offered, display error message and return.  
•	If the student is not enrolled in that course, display error message and return.  
•	If there is no problem, remove student ID from the course’s roster and display a message.  
This function has no return value.
list_courses(id, c_roster)	This function displays and counts courses a student has registered for.  It has two parameters: 
•	id is the ID of the student
•	c_roster is a dictionary of courses offered with their student rosters
This function displays the number of courses the student has registered for and which courses they are.  This function has no return value.

Module: billing.py
You must define the following function in the billing module.

Function	Specification
display_bill (id, s_in_state, c_rosters, c_hours)	This function the student's bill.  It has four parameters: 
•	id is the ID of the student 
•	s_in_state is a dictionary of in state students
•	c_rosters is a dictionary of class rosters
•	c_hours is a dictionary with the credit hours of each class 

This function calculates the bill based on $225 per credit hour for in-state students and $850 per credit hour for out-of-state students. This function has no return value. It will display the student's bill as shown below.


The display_bill function will display the tuition bill for the student using formatted text. Here's an example of a bill displayed for a student:

Tuition Summary
Student: 1001, In-State Student
Generated on 2022-10-13 09:15:38
Course    Hours    Cost  
------    -----  --------
CSC101        3  $ 675.00
CSC102        4  $ 900.00
CSC104        3  $ 675.00
        -------  --------
Total        10  $2250.00

Notes:
•	To print the date and time, you will need to research the datetime library package available in the Python standard library. In particular, that library package contains a module that is also called datetime and a function called now that will be useful.
•	The date and time should represent the when the date is being generated. It should have a 4 digit year, 2 digit month, and 2 digit day. It should NOT include the microseconds in the time.
•	There are two ways to format the time:
o	You can use the strftime function that is included with the datetime module.
o	You can use f-strings using the datetime formatting codes. 
Module: registration.py (main module)
You must define the following functions in the main module.

Function	Specification
login(id, s_list)	This function allows a student to log in.  It has two parameters: 
•	id is the ID of the student
•	s_list, which is the student list
This function asks user to enter PIN. If the ID and PIN combination is in s_list, display message of verification and return True.  Otherwise, display error message and return False.
main()	This function manages the whole registration system.  It has no parameter.  It creates lists and dictionaries to store data: student list, in-state students, courses and hours, maximum class size list and roster list.  It uses a loop to serve multiple students.  Inside the loop, ask user to enter ID, and call the login function to verify student’s identity.  If login is successful, use a loop to allow a student to choose to add courses, drop courses or list courses the student has registered for or if they want to display a bill. This function has no return value.


This program uses lists and dictionaries to store data. To make grading easier, data will be added to these variables at the beginning of the main function.

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

There are 4 students in this program.  ID and PIN of students are stored as tuples in student_list.  The first element of each tuple is student ID and the second element is the PIN.

Students that are in-state are stored in the student_in_state dictionary. Students 1001 and 1003 are in-state students.

Four courses are offered. Each course has a number of credit hours. The courses and credit hour information are stored in course_hours: 
•	CSC101 has 3 credit hours. 
•	CSC102 has 4 credit hours. 
•	CSC103 has 5 credit hours. 
•	CSC104 has 3 credit hours.

The maximum class size of the courses offered are stored in course_max_size.  The max sizes of CSC101, CSC102, CSC103, and CSC104 are 3, 2, 1, and 3 respectively.

Rosters of the four classes offered are stored as four lists which are values of the course_roster dictionary:  
•	Students 1004 and 1003 are enrolled in CSC101.  
•	Student 1001 is enrolled in CSC102.  
•	Student 1002 is enrolled in CSC103. 
•	No one is enrolled in CSC104.

The data given above must be used in the program as specified above. Any changes to how the data is structured must be proposed as a specification change to the instructor and approved by the instructor.

The program should have a loop to create multiple student sessions.  In each session, ask the user to enter an ID, then call the login function to verify the student’s identity.  If login is successful, use a loop to allow the student to add courses, drop courses, list courses registered, or display a bill.

The following is an example execution of the program:


Enter ID to log in, or 0 to quit: 1234
Enter PIN: 123
ID or PIN incorrect

Enter ID to log in, or 0 to quit: 1001
Enter PIN: 111
ID and PIN verified

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC121
Course not found

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC102
You are already enrolled in that course.

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC103
Course already full.

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC101
Course added

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 4
Tuition Summary
Student: 1001, In-State Student
Generated on 2022-10-14 12:35:05
Course    Hours    Cost  
------    -----  --------
CSC101        3  $ 675.00
CSC102        4  $ 900.00
        -------  --------
Total         7  $1575.00

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 2
Enter course you want to drop: CSC121
Course not found

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 2
Enter course you want to drop: CSC103
You are not enrolled in that course.

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 2
Enter course you want to drop: CSC102
Course dropped

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC101
Total number: 1

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC102
Course added

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 4
Tuition Summary
Student: 1001, In-State Student
Generated on 2022-10-14 12:36:20
Course    Hours    Cost  
------    -----  --------
CSC101        3  $ 675.00
CSC102        4  $ 900.00
        -------  --------
Total         7  $1575.00

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 0
Session ended.

Enter ID to log in, or 0 to quit: 1002
Enter PIN: 222
ID and PIN verified

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC103
Total number: 1

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC101
Course already full.

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 1
Enter course you want to add: CSC102
Course added

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 3
Courses registered:
CSC102
CSC103
Total number: 2

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 4
Tuition Summary
Student: 1002, Out-of-State Student
Generated on 2022-10-14 12:36:59
Course    Hours    Cost  
------    -----  --------
CSC102        4  $3400.00
CSC103        5  $4250.00
        -------  --------
Total         9  $7650.00

Enter 1 to add course, 2 to drop course,
3 to list courses, 4 to show bill, 0 to exit: 0
Session ended.

Enter ID to log in, or 0 to quit: 0

