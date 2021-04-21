
# Students first and last name
# Enter the first name
first_name = input("Enter First name:")

# Enter the last name
last_name = input("Enter Last name:")

full_name = (first_name + "," + last_name)

# Enter the phone number
phone_number = input("Enter phone number:")

# Student ID number
student_ID_number = input("Enter Student ID number:")

# Student mailing address
# Enter the mailing
mailing_address1 = input("Enter mailing address:")

# Student City
mailing_address2 = input("Enter City:")

# Student Country/Region
mailing_address3 = input("Enter Country/Region:")

# Student is from Africa use A as an output if the student is not from Africa then use O
native = str(input("Are you from Africa(Y/N):"))

# Students Email
email = input("Enter E-mail:")

student_gender = str(input("Enter the student's gender[M] for Male or [F] for Female: "))
# Students average score of Quiz1 Quiz2 Quiz3 Test1 and Test2

Quiz1 = float(input("enter Quiz1 score **out of 100** : "))
Quiz2 = float(input("enter Quiz2 score **out of 100** : "))
Quiz3 = float(input("enter Quiz3 score **out of 100** : "))
Test1 = float(input("enter Test1 score **out of 100** : "))
Test2 = float(input("enter Test2 score **out of 100** : "))
average_score = float(((Quiz1 + Quiz2 + Quiz3 + Test1 + Test2) / 500) * 100)

# Display student score on zoom call [0-9] points
zoom_score = int(input("Enter zoom attendance score **numbers from 0-9**:"))

# Display student score on homework and assignments [0-10] points
homework_score = int(input("Enter homework assignment score **numbers from 0-10**:"))

# If student is not based in Africa then do not offer them the scholarship only offer it if they are from Africa

if native == "Y":
    native1 = "A"
    if student_gender == "M":
        if average_score >= 80:
            scholarship_candidate = "Yes"
        else:
            scholarship_candidate = "No"
    elif student_gender == "F":
        if average_score >= 76:
            scholarship_candidate = "Yes"
        else:
            scholarship_candidate = "No"
    else:
        student_gender = input("Use M or F for student's gender: ")
else:
    native1 = "O"
    scholarship_candidate = "No"

# format an appropriate output
print("Student's Full name (First,Last): " + full_name)
print("Student's Phone number: " + phone_number)
print("Student's ID number: " + student_ID_number)
print("Student's Mailing address: " + mailing_address1)
print("Student's City residence: " + mailing_address2)
print("Student's Country/Region of residence: " + mailing_address3)
print("African region: " + native1)
print("Student's Quiz and Test average: " + str(average_score))
print("Student's Gender: " + student_gender)
print("Student's Attendance score: " + str(zoom_score))
print("Student's Homework score: " + str(homework_score))
print("Scholarship candidate: " + scholarship_candidate)
