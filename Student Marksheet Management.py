import mysql.connector as p

# Establish connection to the database
cn = p.connect(host='localhost', user='root', passwd='dev@nsh28', database='school')
cur = cn.cursor()

def check():
    if cn.is_connected():
        print("Connected successfully!")

def disp():
    q = "SELECT * FROM student;"
    cur.execute(q)
    r = cur.fetchall()
    if r:
        for i in r:
            print(i)
    else:
        print("No records found.")

def search():
    m = input("Enter name of student to be searched: ")
    q = "SELECT * FROM student WHERE name = %s;"
    cur.execute(q, (m,))
    r = cur.fetchall()
    if r:
        for i in r:
            print(i)
    else:
        print("No student found with that name.")

def add_rec():
    try:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        english = int(input("Enter English marks (0-100): "))
        physics = int(input("Enter Physics marks (0-100): "))
        chemistry = int(input("Enter Chemistry marks (0-100): "))
        maths = int(input("Enter Maths marks (0-100): "))
        cs = int(input("Enter CS marks (0-100): "))

        # Validate marks
        if any(mark < 0 or mark > 100 for mark in [english, physics, chemistry, maths, cs]):
            print("Marks must be between 0 and 100.")
            return

        q = "INSERT INTO student (roll_no, name, english, physics, chemistry, maths, cs) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cur.execute(q, (roll_no, name, english, physics, chemistry, maths, cs))
        cn.commit()  # Save the changes
        print("Record added successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for roll number and marks.")
    except p.Error as err:
        print(f"Database error: {err}")
    except Exception as err:
        print(f"Error: {err}")

def update():
    try:
        RN = int(input("Enter Roll No to update: "))
        maths = int(input("Enter new Maths marks: "))
        english = int(input("Enter new English marks: "))
        
        # Validate marks
        if maths < 0 or maths > 100 or english < 0 or english > 100:
            print("Marks must be between 0 and 100.")
            return

        q = "UPDATE student SET maths = %s, english = %s WHERE roll_no = %s;"
        cur.execute(q, (maths, english, RN))
        cn.commit()
        print("Record updated successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for roll number and marks.")
    except p.Error as err:
        print(f"Database error: {err}")
    except Exception as err:
        print(f"Error: {err}")

def del_REC():
    try:
        RN = int(input("Enter Roll No of student to be deleted: "))
        q = "DELETE FROM student WHERE roll_no = %s;"
        cur.execute(q, (RN,))
        cn.commit()
        print("Record deleted successfully!")
    except p.Error as err:
        print(f"Database error: {err}")
    except Exception as err:
        print(f"Error: {err}")

def con_close():
    if cur is not None:
        cur.close()
    if cn.is_connected():
        cn.close()
        print("Connection closed.")

def menu():
    print("|______________________________|")
    print("|   MARKSHEET Management       |")
    print("|______________________________|")
    print("| MENU:                        |")
    print("| 1. Add Record                |")
    print("| 2. Search Record             |")
    print("| 3. Update Record             |")
    print("| 4. Delete Record             |")
    print("| 5. Display All Records       |")
    print("| 0. Exit                      |")
    print("|______________________________|")

# Main code
if __name__ == "__main__":
    check()  # Check connection status
    while True:
        menu()
        ch = int(input("Enter Choice: "))
        if ch == 1:
            add_rec()
        elif ch == 2:
            search()
        elif ch == 3:
            update()
        elif ch == 4:
            del_REC()
        elif ch == 5:
            disp()
        elif ch == 0:
            break
        else:
            print("Invalid choice. Please try again.")

        print("Press 'y' to continue or 'n' to stop.")
        n = input("y/n: ")
        if n.lower() != 'y':
            break

    con_close()  # Close connection when done
