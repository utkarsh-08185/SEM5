# ----- Using a List to Store All Students -----
students_list = []

# ----- Using a Set to Ensure Unique Roll Numbers -----
roll_number_set = set()

# ----- Using a Dictionary (Map) to Store Student Data by Roll Number -----
students_map = {}

# --- Function to Add a Student ---
def add_student(roll_no, name, dob, address):
    if roll_no in roll_number_set:
        print(f"Roll No {roll_no} already exists. Cannot add duplicate.")
        return
    
    # Store student as a dictionary
    student = {
        'roll_no': roll_no,
        'name': name,
        'dob': dob,
        'address': address
    }

    # Add to List
    students_list.append(student)

    # Add to Set
    roll_number_set.add(roll_no)

    # Add to Map
    students_map[roll_no] = student

    print(f"Student with Roll No {roll_no} added successfully.\n")

# --- Function to Display All Students ---
def display_students():
    print("\n--- All Students (from List) ---")
    for student in students_list:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, DOB: {student['dob']}, Address: {student['address']}")

    print("\n--- Roll Numbers (from Set) ---")
    print(roll_number_set)

    print("\n--- Student Info by Roll No (from Map) ---")
    for roll_no, student in students_map.items():
        print(f"{roll_no} => {student}")

# --- Add Students ---
add_student(101, "Alice Smith", "2001-05-10", "New York")
add_student(102, "Bob Johnson", "2000-08-23", "Los Angeles")
add_student(103, "Charlie Brown", "2002-12-15", "Chicago")
add_student(101, "Duplicate Roll", "1999-01-01", "Nowhere")  # This will be rejected

# --- Display All Students ---
display_students()
