import mysql.connector as con

database=con.connect(host="localhost",user="root",password="Imgonakillu@98",database="School")
print("connection created")

cur=database.cursor()
#cur.execute("create database School")
#print("Database created")
#cur.execute("CREATE TABLE STUDENT(ID INT NOT NULL AUTO_INCREMENT, NAME VARCHAR(50) NOT NULL,AADHAR_NUMBER VARCHAR(20) NOT NULL,FATHER_NAME VARCHAR(50) NOT NULL,MOBILE_NO VARCHAR(20) NOT NULL,CLASS INT NOT NULL,CITY VARCHAR(20) NOT NULL,PASSWORD VARCHAR(50) NOT NULL,PRIMARY KEY(ID))")
#cur.execute("CREATE TABLE EMPLOYEE(ID INT NOT NULL AUTO_INCREMENT, NAME VARCHAR(50) NOT NULL,MOBILE_NO VARCHAR(20) NOT NULL,DESIGNATION INT NOT NULL,CITY VARCHAR(20) NOT NULL,PASSWORD VARCHAR(50) NOT NULL,PRIMARY KEY(ID))")
#cur.execute("CREATE TABLE CLASS(CLASS_ID INT NOT NULL AUTO_INCREMENT,CLASS_NAME VARCHAR(20) NOT NULL,PRIMARY KEY(CLASS_ID))")
#classes=[("9",),("10",),("11",),("12",)]
#cur.executemany("INSERT INTO CLASS(CLASS_NAME) VALUES (%s)",classes)
#database.commit()
#print("Table created")
#cur.execute("TRUNCATE table EMPLOYEE")


std_ID=521200
emp_ID=621200


def ID_generator(role):
    global std_ID,emp_ID
    if role == 'student':
        std_ID+=1
        return std_ID
    elif role =='employee':
        emp_ID += 1
        return emp_ID
    else:
        return None
    
def Sign_up(role):
    while True:

        if role=='student':
            a=0
            m=0
            std_id=ID_generator(role)
            Name=input("Enter your Name: ")
            while True:
                Aadhar=input("Enter 12 Digit AADHAR number: ")
                l=len(Aadhar)
                if l==12:
                    d=Aadhar.isdigit()
                    if d==True:
                        a=1
                        break
                else:
                    print("INVALID AADHAR NUMBER!!!")
                i=int(input("press 1 to Input again: "))
                
            Father=input("Father's Name: ")
            Num=input("Mobile Number: ")
            Class=input("Your class: ")
            City=input("City you live in: ")
            Password=input("Create your password: ")

            cur.execute("SELECT * FROM CLASS WHERE CLASS_NAME = %s", (Class,))
            class_data = cur.fetchone()

            cur.execute("INSERT INTO STUDENT(ID,NAME,AADHAR_NUMBER,FATHER_NAME,MOBILE_NO,CLASS,CITY,PASSWORD) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(std_id,Name,str(Aadhar),Father,str(Num),Class,City,Password))
            
        if role=='employee':
            emp_id=ID_generator(role)
            Name=input("Enter your Name: ")
            Num=input("Mobile Number: ")
            Designation=input("Class you teach: ")
            City=input("City you live in: ")
            Password=input("Create your password: ")
            cur.execute("INSERT INTO EMPLOYEE(ID,NAME,MOBILE_NO,DESIGNATION,CITY,PASSWORD) VALUES(%s,%s,%s,%s,%s,%s)",(emp_id,Name,str(Num),Designation,City,Password))

        database.commit()

        print("Registration done successfully your userID is: ",std_id if role == 'student' else emp_ID)

        i=int(input("Press 1 to SIGN UP again\n"
                        "Press 0 to for LOG IN\n"
                        "Enter your choice: "))
        if i==0:
            break;

        
def Log_in():
    user=input("Enter user ID: ")
    password=input("Enter your password: ")
    f=0
    
    cur.execute("select * from student where ID = %s",(user,))
    data=cur.fetchone()
        
    if data:
        if password==data[7]:
            f=1
            print("Welcome ",data[1])
            student(data[5])
        else:
            print("Invalid password Try Again")
    


    cur.execute("select * from employee where ID = %s",(user,))
    data=cur.fetchone()
        
    if data:
        if password==data[5]:
            f=1
            print("Welcome ",data[1])
            employee(data[3])
        else:
            print("Invalid password Try Again")

    if f==0:
        print("UserID doesn't Exist")



def student(student_class):
    while True:
        print("\nStudent Panel:")
        print("1. View Students of Your Class")
        print("2. Update Your Data")
        print("0. Exit Student Panel")

        choice = input("Enter your choice: ")

        if choice == '1':
            cur.execute("SELECT * FROM STUDENT WHERE CLASS = %s", (student_class,))
            students = cur.fetchall()
            print("\nList of students in Class", student_class)
            for student in students:
                print("Student ID:", student[0], "Name:", student[1], "Aadhar:", student[2],
                      "Father's Name:", student[3], "Mobile No:", student[4], "City:", student[6])
            print("\n")

        elif choice == '2':
            std_id=input("Enter your ID: ")
            std_update(std_id)

            
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
        
    

def std_Update(ID):
    while True:
        print("1. Update Name")
        print("2. Update Aadhar Card Number")
        print("3. Update Father's Name")
        print("4. Update Mobile Number")
        print("5. Update City")
        print("6. Update Password")
        print("0. Exit Update Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter your Updated Name: ")
            cur.execute("UPDATE STUDENT SET NAME = %s WHERE ID = %s", (new_name, ID))
            print("Name updated Successfully")

        elif choice == '2':
            new_aadhar = input("Enter your Updated Aadhar Card Number: ")
            cur.execute("UPDATE STUDENT SET AADHAR_NUMBER = %s WHERE ID = %s", (new_aadhar, ID))
            print("Aadhar Number Updated")

        elif choice == '3':
            new_father_name = input("Enter your Updated Father's Name: ")
            cur.execute("UPDATE STUDENT SET FATHER_NAME = %s WHERE ID = %s", (new_father_name, ID))
            print("Father's Name updated")

        elif choice == '4':
            new_mobile = input("Enter your Updated Mobile Number: ")
            cur.execute("UPDATE STUDENT SET MOBILE_NO = %s WHERE ID = %s", (new_mobile, ID))
            print("Mobile Number updated")

        elif choice == '5':
            new_city = input("Enter your Updated City: ")
            cur.execute("UPDATE STUDENT SET CITY = %s WHERE ID = %s", (new_city, ID))
            print("City Name updated")

        elif choice == '6':
            new_pass=input("Enter New Password: ")
            cur.execute("UPDATE STUDENT SET PASSWORD = %s WHERE ID = %s", (new_pass, ID))
            print("Password Updated")

        elif choice == '0':
            print("\n")
            break
        else:
            print("Invalid choice. Please try again.")
            print("\n")

            
        database.commit()
        
def employee(designation):
    while True:
        print("\nEmployee Panel:")
        print("1. Details of All Employees")
        print("2. View Students of Your Class")
        print("3. Your Details")
        print("4. Update Your Data")
        print("0. Exit Employee Panel")

        choice = input("Enter your choice: ")
        
        if choice =='1':
            cur.execute("SELECT * FROM EMPLOYEE")
            employees = cur.fetchall()
            print("\nList of all employees:")
            for employee in employees:
                print("Employee ID:", employee[0], "Name:", employee[1], "Mobile No:", employee[2],
                      "Designation:", employee[3], "City:", employee[4])
            print('\n')

        if choice == '2':
            cur.execute("SELECT * FROM STUDENT WHERE CLASS = %s", (designation,))
            students = cur.fetchall()
            print("\nList of students in Class", designation)
            for student in students:
                print("Student ID:", student[0], "Name:", student[1], "Aadhar:", student[2],
                      "Father's Name:", student[3], "Mobile No:", student[4], "City:", student[6])
            print("\n")

        elif choice == '3':
            cur.execute("SELECT * FROM EMPLOYEE WHERE CLASS = %s", (designation,))
            emps = cur.fetchone()
            print("\nYOUR Class", designation)
            for emp in emps:
                print("ID:", emp[0], "Name:", emp[1], "Mobile No:", emp[2],
                      "Designation:", student[3], "City:", student[4])
            print("\n")

        elif choice == '4':
            emp_id=input("Enter your ID: ")
            emp_update(emp_id)

            
        elif choice == '0':
            print("\n")
            break
        else:
            print("Invalid choice. Please try again.")
            print("\n")
        
def emp_update(ID):
    while True:
        print("1. Update Name")
        print("2. Update Mobile Number")
        print("3. Update Designation")
        print("4. Update City")
        print("5. update password")
        print("0. Previous Menu")
        
        
        choice=input("Enter your choice: ")

        if choice == '1':
            new_name=input("Enter New Name: ")
            cur.execute("update employee set NAME = %s where ID = %s", (new_name,ID))
            print("Name updated successfully")

        elif choice == '2':
            new_num=input("Enter your New Number: ")
            cur.execute("update employee set MOBILE_NO = %s where ID =%s",(new_num,ID))
            print("Mobile Number Udpated")

        elif choice == '3':
            new_des=input("Enter your Designation: ")
            cur.execute("update employee set DESIGNATION = %s where ID =%s",(new_des,ID))
            print("Designation updated")

        elif choice == '4':
            new_city=input("Enter your City: ")
            cur.execute("update employee set CITY = %s where ID =%s",(new_city,ID))
            print("City Updated")

        elif choice == '5':
            new_pass=input("Enter new Password: ")
            cur.execute("update employee set PASSWORD = %s where ID =%s",(new_pass,ID))
            print("Password Updated successfully")

        elif choice == '0':
            print("\n")
            break
        else:
            print("Invalid choice. Please try again.")

            
        database.commit()

                


    
        
while True:
    i=input("Press 1 for LOG IN\n"
            "Press 2 for SIGN UP\n"
            "Press 0 to Exit Portal\n"
            "Enter your choice: ")
    if i=='2':
        role=input("Enter role (student/employee): ")
        Sign_up(role.lower())
    elif i=='1':
        Log_in()
    elif i=='0':
        print("Signing OFF")
        break;
    else:
        break;
