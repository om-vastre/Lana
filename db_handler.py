import sqlite3

student_data = [
    (101, 'Amit Kumar', 'A', 2, 'Computer Science', '9876543210', 'amit.kumar@example.com', 85.5, 8.2, 8.5, 8.7, 9.0, 8.8, 8.9, 9.2, 9.1, 8.8, 'Mathematics, Programming, Data Structures'),
    (102, 'Priya Sharma', 'B', 3, 'Electrical Engineering', '8765432109', 'priya.sharma@example.com', 92.0, 8.9, 9.0, 9.2, 9.5, 9.3, 9.1, 9.4, 9.6, 9.3, 'Circuit Theory, Power Systems, Control Systems'),
    (103, 'Rahul Singh', 'A', 4, 'Mechanical Engineering', '7654321098', 'rahul.singh@example.com', 88.3, 8.5, 8.7, 8.9, 9.1, 8.8, 9.0, 9.2, 9.0, 8.9, 'Thermodynamics, Fluid Mechanics, Manufacturing Processes'),
    (104, 'Neha Patel', 'B', 2, 'Civil Engineering', '6543210987', 'neha.patel@example.com', 87.1, 8.0, 8.3, 8.6, 8.9, 8.7, 8.8, 8.5, 8.7, 8.4, 'Structural Analysis, Concrete Technology, Geotechnical Engineering'),
    (105, 'Ankit Gupta', 'C', 3, 'Electronics and Communication', '5432109876', 'ankit.gupta@example.com', 91.7, 8.7, 8.9, 9.1, 9.3, 9.0, 9.2, 9.4, 9.2, 9.1, 'Analog Circuits, Digital Signal Processing, Communication Systems'),
    (106, 'Sneha Desai', 'A', 4, 'Computer Science', '7564892134', 'sneha.desai@example.com', 87.8, 8.3, 8.6, 8.9, 9.2, 9.0, 9.1, 9.3, 9.0, 8.9, 'Database Management, Software Engineering, Operating Systems'),
    (107, 'Ravi Singh', 'B', 3, 'Electrical Engineering', '6457821349', 'ravi.singh@example.com', 89.5, 8.8, 9.1, 9.3, 9.6, 9.4, 9.2, 9.5, 9.4, 9.2, 'Power Electronics, Electric Machines, Renewable Energy Systems'),
    (108, 'Pooja Sharma', 'A', 2, 'Mechanical Engineering', '5248697138', 'pooja.sharma@example.com', 90.2, 8.9, 9.0, 9.2, 9.4, 9.1, 9.3, 9.1, 9.0, 8.9, 'Machine Design, Thermal Engineering, Robotics'),
    (109, 'Karan Patel', 'B', 3, 'Civil Engineering', '4139578264', 'karan.patel@example.com', 86.7, 8.1, 8.4, 8.7, 9.0, 8.8, 8.9, 8.6, 8.8, 8.5, 'Structural Dynamics, Transportation Engineering, Environmental Engineering'),
    (110, 'Shreya Gupta', 'C', 4, 'Electronics and Communication', '3028467951', 'shreya.gupta@example.com', 93.1, 9.0, 9.2, 9.4, 9.7, 9.5, 9.3, 9.6, 9.5, 9.4, 'Digital Electronics, Microprocessors, Wireless Communication'),
    (111, 'Rahul Mehta', 'A', 3, 'Computer Science', '9876543210', 'rahul.mehta@example.com', 88.5, 8.4, 8.7, 9.0, 9.2, 9.1, 9.3, 9.1, 9.0, 8.8, 'Data Structures, Algorithms, Operating Systems'),
    (112, 'Sanya Verma', 'B', 4, 'Electrical Engineering', '8765432109', 'sanya.verma@example.com', 91.2, 8.9, 9.1, 9.3, 9.5, 9.4, 9.2, 9.6, 9.4, 9.3, 'Control Systems, Power Systems, Renewable Energy'),
    (113, 'Amit Singhania', 'A', 2, 'Mechanical Engineering', '7654321098', 'amit.singhania@example.com', 85.7, 8.0, 8.3, 8.6, 8.9, 8.7, 8.8, 8.5, 8.7, 8.4, 'Thermodynamics, Fluid Mechanics, Engineering Drawing'),
    (114, 'Nisha Patel', 'B', 3, 'Civil Engineering', '6543210987', 'nisha.patel@example.com', 89.1, 8.6, 8.8, 9.0, 9.2, 9.1, 9.3, 9.0, 8.9, 8.7, 'Structural Analysis, Geotechnical Engineering, Construction Management'),
    (115, 'Vivek Sharma', 'C', 4, 'Electronics and Communication', '5432109876', 'vivek.sharma@example.com', 92.3, 9.1, 9.3, 9.5, 9.7, 9.6, 9.4, 9.7, 9.6, 9.5, 'Analog Circuits, Digital Signal Processing, Communication Networks'),
    (116, 'Riya Singh', 'A', 2, 'Computer Science', '9876543210', 'riya.singh@example.com', 86.5, 8.1, 8.4, 8.7, 9.0, 8.8, 8.9, 9.1, 8.9, 8.7, 'Data Structures, Algorithms, Database Systems'),
    (117, 'Kunal Shah', 'B', 3, 'Electrical Engineering', '8765432109', 'kunal.shah@example.com', 90.7, 8.8, 9.0, 9.2, 9.4, 9.1, 9.3, 9.5, 9.3, 9.1, 'Power Systems, Control Systems, Renewable Energy'),
    (118, 'Deepika Mishra', 'A', 4, 'Mechanical Engineering', '7654321098', 'deepika.mishra@example.com', 87.9, 8.3, 8.6, 8.9, 9.1, 8.8, 9.0, 9.2, 9.0, 8.9, 'Thermal Engineering, Manufacturing Processes, Machine Design'),
    (119, 'Rahul Gupta', 'B', 2, 'Civil Engineering', '6543210987', 'rahul.gupta@example.com', 88.4, 8.2, 8.5, 8.8, 9.0, 8.7, 8.9, 8.6, 8.8, 8.5, 'Structural Analysis, Concrete Technology, Transportation Engineering'),
    (120, 'Neha Singh', 'C', 3, 'Electronics and Communication', '5432109876', 'neha.singh@example.com', 91.5, 8.7, 8.9, 9.1, 9.3, 9.0, 9.2, 9.4, 9.2, 9.1, 'Analog Circuits, Digital Signal Processing, Communication Systems'),
    (121, 'Amit Kumar', 'A', 3, 'Computer Science', '9876543210', 'amit.kumar@example.com', 88.2, 8.4, 8.7, 9.0, 9.2, 9.1, 9.3, 9.1, 9.0, 8.8, 'Data Structures, Algorithms, Software Engineering'),
    (122, 'Priya Patel', 'B', 4, 'Electrical Engineering', '8765432109', 'priya.patel@example.com', 90.5, 8.9, 9.1, 9.3, 9.5, 9.4, 9.2, 9.6, 9.4, 9.3, 'Power Systems, Control Systems, Renewable Energy'),
    (123, 'Rahul Verma', 'A', 2, 'Mechanical Engineering', '7654321098', 'rahul.verma@example.com', 87.8, 8.3, 8.6, 8.9, 9.1, 8.8, 9.0, 9.2, 9.0, 8.9, 'Thermal Engineering, Manufacturing Processes, Machine Design'),
    (124, 'Neha Gupta', 'B', 3, 'Civil Engineering', '6543210987', 'neha.gupta@example.com', 88.9, 8.6, 8.8, 9.0, 9.2, 9.1, 9.3, 9.0, 8.9, 8.7, 'Structural Analysis, Geotechnical Engineering, Construction Management'),
    (125, 'Karan Singh', 'C', 4, 'Electronics and Communication', '5432109876', 'karan.singh@example.com', 92.0, 9.0, 9.2, 9.4, 9.7, 9.6, 9.4, 9.7, 9.6, 9.5, 'Analog Circuits, Digital Signal Processing, Communication Networks'),
    (126, 'Anjali Sharma', 'A', 2, 'Computer Science', '9876543210', 'anjali.sharma@example.com', 86.7, 8.2, 8.5, 8.8, 9.0, 8.8, 8.9, 9.1, 8.9, 8.7, 'Data Structures, Algorithms, Operating Systems'),
    (127, 'Aryan Patel', 'B', 3, 'Electrical Engineering', '8765432109', 'aryan.patel@example.com', 89.3, 8.8, 9.0, 9.2, 9.4, 9.2, 9.3, 9.5, 9.3, 9.1, 'Power Systems, Control Systems, Renewable Energy'),
    (128, 'Sneha Verma', 'A', 4, 'Mechanical Engineering', '7654321098', 'sneha.verma@example.com', 88.1, 8.3, 8.6, 8.9, 9.1, 8.9, 9.0, 9.2, 9.0, 8.9, 'Thermal Engineering, Manufacturing Processes, Robotics'),
    (129, 'Rohan Gupta', 'B', 2, 'Civil Engineering', '6543210987', 'rohan.gupta@example.com', 87.4, 8.1, 8.4, 8.7, 8.9, 8.8, 8.9, 8.6, 8.8, 8.6, 'Structural Analysis, Concrete Technology, Transportation Engineering'),
    (130, 'Priya Singh', 'C', 3, 'Electronics and Communication', '5432109876', 'priya.singh@example.com', 91.8, 8.7, 8.9, 9.1, 9.3, 9.1, 9.2, 9.4, 9.2, 9.1, 'Analog Circuits, Digital Signal Processing, Communication Systems'),
    (131, 'Aditya Sharma', 'A', 4, 'Computer Science', '9876543210', 'aditya.sharma@example.com', 89.5, 8.6, 8.9, 9.2, 9.4, 9.1, 9.3, 9.0, 8.9, 8.7, 'Data Structures, Algorithms, Machine Learning'),
    (132, 'Shivani Gupta', 'B', 3, 'Electrical Engineering', '8765432109', 'shivani.gupta@example.com', 90.2, 8.8, 9.0, 9.2, 9.4, 9.2, 9.3, 9.5, 9.3, 9.1, 'Power Electronics, Control Systems, Renewable Energy'),
    (133, 'Raj Patel', 'A', 2, 'Mechanical Engineering', '7654321098', 'raj.patel@example.com', 88.3, 8.4, 8.7, 8.9, 9.1, 8.9, 9.0, 9.2, 9.0, 8.9, 'Thermal Engineering, Manufacturing Processes, CAD/CAM'),
    (134, 'Ananya Singh', 'B', 3, 'Civil Engineering', '6543210987', 'ananya.singh@example.com', 87.9, 8.5, 8.8, 9.0, 9.2, 9.0, 9.1, 8.9, 8.8, 8.6, 'Structural Analysis, Geotechnical Engineering, Construction Materials'),
    (135, 'Vivek Sharma', 'C', 4, 'Electronics and Communication', '5432109876', 'vivek.sharma@example.com', 91.0, 8.9, 9.1, 9.3, 9.5, 9.4, 9.2, 9.6, 9.4, 9.2, 'Analog Circuits, Digital Signal Processing, Wireless Communication'),
    (136, 'Mehak Verma', 'A', 2, 'Computer Science', '9876543210', 'mehak.verma@example.com', 86.8, 8.2, 8.5, 8.8, 9.0, 8.8, 8.9, 9.1, 8.9, 8.7, 'Data Structures, Algorithms, Operating Systems'),
    (137, 'Amita Patel', 'B', 3, 'Electrical Engineering', '8765432109', 'amita.patel@example.com', 89.6, 8.9, 9.1, 9.3, 9.5, 9.3, 9.4, 9.6, 9.4, 9.2, 'Power Systems, Control Systems, Power Electronics'),
    (138, 'Ravi Kumar', 'A', 4, 'Mechanical Engineering', '7654321098', 'ravi.kumar@example.com', 88.5, 8.3, 8.6, 8.9, 9.1, 8.8, 9.0, 9.2, 9.0, 8.9, 'Thermal Engineering, Manufacturing Processes, Robotics'),
    (139, 'Priyanka Gupta', 'B', 2, 'Civil Engineering', '6543210987', 'priyanka.gupta@example.com', 87.2, 8.1, 8.4, 8.7, 8.9, 8.8, 8.9, 8.6, 8.8, 8.6, 'Structural Analysis, Concrete Technology, Transportation Engineering'),
    (140, 'Rahul Verma', 'C', 3, 'Electronics and Communication', '5432109876', 'rahul.verma@example.com', 91.2, 8.8, 9.0, 9.2, 9.4, 9.2, 9.3, 9.5, 9.3, 9.1, 'Analog Circuits, Digital Signal Processing, Communication Systems')

]

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS students (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     roll_no INT,
#                     name VARCHAR(255),
#                     division VARCHAR(50),
#                     year INT,
#                     department VARCHAR(100),
#                     mobileno VARCHAR(15),
#                     email VARCHAR(255),
#                     attendance_percentage FLOAT,
#                     sgpa1 FLOAT,
#                     sgpa2 FLOAT,
#                     sgpa3 FLOAT,
#                     sgpa4 FLOAT,
#                     sgpa5 FLOAT,
#                     sgpa6 FLOAT,
#                     sgpa7 FLOAT,
#                     sgpa8 FLOAT,
#                     cgpa FLOAT,
#                     subjects VARCHAR(255)
#                 )''')

# insert_query = '''INSERT INTO students (roll_no, name, division, year, department, mobileno, email, attendance_percentage, sgpa1, sgpa2, sgpa3, sgpa4, sgpa5, sgpa6, sgpa7, sgpa8, cgpa, subjects)
#                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

# cursor.executemany(insert_query, student_data)

# rows = cursor.execute("SELECT * FROM students WHERE subjects LIKE '%Power Electronics%';").fetchall()

# for row in rows:
#     print(row)

# cursor.execute('''CREATE TABLE IF NOT EXISTS notices (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     sender_id INT,
#                     receiver_ids VARCHAR(255),
#                     msg VARCHAR(255)
#                 )''')


# # Define the SQL query to retrieve rows based on receiver_id
# sql = f'''SELECT * 
#             FROM notices 
#             WHERE ? IN (SELECT CAST(receiver_ids AS INTEGER) FROM notices)'''

# receiver_id = 7
# cursor.execute(sql, (receiver_id,))

# rows = cursor.fetchall()
# for row in rows:
#     print(row)


# ids_tuple = tuple([2,3])
# sql = f"DELETE FROM notices WHERE id IN {ids_tuple}"
# cursor.execute(sql)


conn.commit()
conn.close()

print("Data inserted successfully into the 'students' table.")

