from statistics import mean

studentDict = {"Jimmy":[99, 98, 97], "Jane":[92, 91, 90], "Jess":[88, 87, 86]}

def enter():
    print("\n")

def acceptstudentname():
    print("Which Student?")
    while 1:    
        enter()
        enter()
        student = input()
        try:
            enter()
            enter()
            studentDict[student]
        except:
            print("Please type one of the following student names and press enter.")
            enter()
            print(studentDict.keys())
        else:
            return student
        
# Grade entering function

def entergrade():
    student_name = acceptstudentname()
    print("Please enter the new grade for",student_name)
    enter()
    enter()
    while 1:   
        try:
            new_grade = input()
            enter()
            enter()
            if 0 <= int(new_grade) < 101:
                studentDict[student_name].append(int(new_grade))
                print(student_name,"'s grade of",new_grade,"has been added!")
                enter()
                enter()      
                return
            else:
                print("Please enter a number between 0 and 100 and press enter.")
                enter()
                enter()
        except:
            print("Please enter a number between 0 and 100 and press enter.")
            enter()
            enter()


# Student removal function

def removestudent():
    student_name = acceptstudentname()
    studentDict.pop(student_name)
    print(student_name,"has been removed from the class.")
    enter()
    enter()
    #print(studentDict)



# Student grade averaging function

def studentaveragegrades():
    student_name = acceptstudentname()
    average_grade = float(mean(studentDict[student_name]))
    print("The average grade for",student_name,"is",average_grade)
    enter()
    enter()
    #print(studentDict)




##########################################

# Main Menu Loop

##########################################

program_active = 1

while program_active:
    print("   Welcome to Grade Central!")
    enter()
    enter()
    print("   [1] Enter Grades")
    enter()
    print("   [2] Remove a Student")
    enter()
    print("   [3] Student Average Grades")
    enter()
    print("   [4] Exit")
    enter()
    enter()
    print("What would you like to do today?  (Enter a number)")
    enter()
    enter()

    user_input = input()

    if user_input == "1":
        enter()
        enter()
        entergrade()

    elif user_input == "2":
        enter()
        enter()
        removestudent()

    elif user_input == "3":
        enter()
        enter()
        studentaveragegrades()

    elif user_input == "4":
        program_active = 0
        enter()
        enter()
        print("Exiting...")
        enter()
        enter()
        print("Have a nice day!")

    else:
        enter()
        enter()
        print("Please enter a number between 1 and 4 and press enter.")
        enter()
        enter()
    


