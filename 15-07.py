#section A 
l1 = []
print(l1)

l2 = ["arshil","rohit","rohan","rushi","sekhar"]
print(l2)

marks = [99,23,77,89,57,]
print(marks)

intro = ["arshil","ugaon",20, "%87"]
print (intro)

num = [[1,2,3],[4,5,6,],[7,8,9]]
print( num [0:3])

num1 = [[1,2,2],[3,4,5]]
print (num1[0:2:2])

#using lenth method
print(len(l1))

programmers = ["python","java","c++","c+","javascript"]
print("favorite programming languages",programmers)

#section B

city_name = ["nagpur","bombay","puna","nashik","niphad"]
print(city_name[2])

print(city_name[-1])

print(city_name[0:5:3])

print(city_name[::-1])

print (city_name[::2])

print(city_name[0:6:2])


name = [["hello"],["hiii"],["heyyy"],["whtasapp"],["yepp"]]
print(name[2])

#diffrence between (=) and copy() 
#1////  (=)

list1 = [1,2,3]
list2 = list1

list2.append(4)

print (list1,list2)
print(id(l1))
print(id(l2))
#2/// copy()

l1 = [1,2,3]
l2 = l1.copy()

l2.append(4)
print(l1,l2)
print(id(l1))
print(id(l2))


# section c 
l3 = [1,2,3,4,5]
l3[2] = 4
print(l3)

city = ["ugaon","niphad","nashik","maharastra","india"]
city.append("asia")
print(city)


student = ["rohan","roit","anam"]
student.insert(0,"arshil")
print(student)

student1 = ["arshil","rohan"]
marks = [89,76]
student1.extend(marks)
print(student1)

# section D 

name = ["arshil","rohit","viki","darshan"]
name[::-2] = ["sohel","vikas"]
print(name)

shopping_list = ["fruits","tech product","grosary","sea food"]
shopping_list [0]= "milk"
print(shopping_list)

#append we use for add the item in list 
name4 = ["shaikh","pathan"]
name4.append("shah")
print(name4)

#extend we use for merge to list in one or add elements to anoter colleation
name5 = [1,2,3]
name6 = [9,8,7]
name5.extend(name6)
print(name5)

#that is diffrence is append is use for add one item in list
# and extend is merge two list in one 

empolyee1 = ["gita","soham","roshan"]
empolyee2 = ["vina","nadim","sarthak"]
empolyee1.extend(empolyee2)
print(empolyee1)

"""

choise = int(input("Enter your chiose:"))
match "choise":
    case "choise=1":
        print("add student")
    case "choise=2":
        print("insert student")
    case "choise=3":
        print("update student")
    case "choise=4":
        print("update student")
    case "choise=5":
        print("exist")
    case _:
        print("invalid choise")
        """


# ==========================================
# Student Management System
# ==========================================

students = []

while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Insert Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        # -------------------------------
        # Add Student
        # -------------------------------
        case 1:
            name = input("Enter Student Name: ")
            students.append(name)
            print("Student Added Successfully.")

        # -------------------------------
        # Insert Student
        # -------------------------------
        case 2:
            name = input("Enter Student Name: ")
            index = int(input("Enter Position: "))

            if 0 <= index <= len(students):
                students.insert(index, name)
                print("Student Inserted Successfully.")
            else:
                print("Invalid Position.")

        # -------------------------------
        # Update Student
        # -------------------------------
        case 3:
            if len(students) == 0:
                print("No Students Available.")
            else:
                print("\nStudent List")
                for i in range(len(students)):
                    print(i, "->", students[i])

                index = int(input("Enter Student Index to Update: "))

                if 0 <= index < len(students):
                    new_name = input("Enter New Name: ")
                    students[index] = new_name
                    print("Student Updated Successfully.")
                else:
                    print("Invalid Index.")

        # -------------------------------
        # Display Students
        # -------------------------------
        case 4:
            if len(students) == 0:
                print("No Students Found.")
            else:
                print("\n------ Student List ------")
                for i in range(len(students)):
                    print(i, ":", students[i])

        # -------------------------------
        # Exit
        # -------------------------------
        case 5:
            print("Thank You!")
            break

        # -------------------------------
        # Invalid Choice
        # -------------------------------
        case _:
            print("Invalid Choice. Please Try Again.")


