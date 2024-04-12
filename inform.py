import requests
import sqlite3
from tabulate import tabulate

gen_url = 'http://localhost:11434/api/generate'


def create_query(query):

    # query = "give me list of students enrolled for Data Structures subject"
    data = {
    "model": "gemma",
    "prompt":"Table name : students\nColumns & Column info :\n1. id : id of student user, datatype int\n2.roll_no: Roll no of students, datatype int\n3.name: Name of student, datatype varchar\n4.division: division of student, datatype varchar\n5.year: year of study, datatype int\n6.department : engineering department of students, datatype varchar\n7.mobileno: mobile no of student, datatype varchar\n8.email: email id of students, datatype varchar\n9.attendance_percentage: attendance in percentage, datatype float\n10. sgpa1: Semester Grade Point Average of first semester, datatype float\n11. sgpa2: Semester Grade Point Average of second semester, datatype float\n12.sgpa3: Semester Grade Point Average of third semester, datatype float\n13.sgpa4: Semester Grade Point Average of fourth semester, datatype float\n14.sgpa5: Semester Grade Point Average of fifth semester, datatype float\n15.sgpa6: Semester Grade Point Average of sixth semester, datatype float\n16.sgpa7: Semester Grade Point Average of seventh semester, datatype float\n17.sgpa8: Semester Grade Point Average of eighth semester, datatype float\n18.cgpa: Cumulative Grade Point Average, datatype float\n19.subjects: comma-separated list of names of subjects enrolled by students, datatype varchar \n\nI have a sqlite3 database table as described above which consists of given columns and my query is '"+query+"', for this create a simple SELECT sqlite3 query to get id and roll_no of all students who satisfies criteria given in query and also extract the message in query. Relpy in following format:\nsqlite3 Query:\n {query here} \nMessage : {message}",
    "stream": False,
    "options": {
        # "num_ctx" : 4196,
        # "num_gpu" : 42
        "num_gpu" : 2
        }
    }

    x = requests.post(gen_url, json = data)
    resp = x.json()
    print(resp['response'])

    if resp:
        return resp['response']
    else:
        None


def extract_sql_query(text):

    query = text[text.find("```sql")+6:]
    query = query[:query.find("```")]
    if query[0]==" ":
        query = query[1:]

    msg = text[text.find("**Message:**")+13:]

    if query:
        print("\n\nExtracted SQL Query: ")
        print(query)
        return query, msg
    else:
        return None


def retrive_student_list(extracted_query):
    if extracted_query:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        rows = cursor.execute(extracted_query).fetchall()
        print("Retrived students IDs : ")
        for row in rows:
            print(row[0])
        connection.close()
        return rows
    else:
        print("No SQL query found in the input text.")


def add_notice(sender_id, sorted_students, msg):
    student_list = ""
    for each_student in sorted_students:
        student_list = student_list + str(each_student[0]) + ","
    
    print("Sender : ", sender_id)
    print("Receiver : ", student_list)
    print("Msg : ", msg)

    try:
        sql = '''INSERT INTO notices (sender_id, receiver_ids, msg) 
        VALUES (?, ?, ?)'''
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute(sql, (sender_id, student_list, msg))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        return False


def main(ID, prompt):
    SENDER_ID = ID

    # responce = create_query("Infrom to all students enrolled for Power Electronics subject to attend today's session.")
    responce = create_query(prompt)

    print("Responce : ", responce)
    if responce != None:
        extracted_query, msg = extract_sql_query(responce)
        if extracted_query != None:
            sorted_students = retrive_student_list(extracted_query)
            final_responce = add_notice(SENDER_ID, sorted_students, msg)
            if final_responce:
                print("\nNotice added successfully.")
            else:
                print(f"\nFailed to add notice.")
        else:
            print("Error : Query not found in responce!!")
    else:
        print("Error : Model failed to generate responce!!")

    # connection.close()


if __name__  == "__main__":
    print("running this file")




# Table name : students\nColumns & Column info :\n1. id : id of student user, datatype int\n2.roll_no: Roll no of students, datatype int\n3.name: Name of student, datatype varchar\n4.division: division of student, datatype varchar\n5.year: year of study, datatype int\n6.department : engineering department of students, datatype varchar\n7.mobileno: mobile no of student, datatype varchar\n8.email: email id of students, datatype varchar\n9.attendance_percentage: attendance in percentage, datatype float\n10. sgpa1: Semester Grade Point Average of first semester, datatype float\n11. sgpa2: Semester Grade Point Average of second semester, datatype float\n12.sgpa3: Semester Grade Point Average of third semester, datatype float\n13.sgpa4: Semester Grade Point Average of fourth semester, datatype float\n14.sgpa5: Semester Grade Point Average of fifth semester, datatype float\n15.sgpa6: Semester Grade Point Average of sixth semester, datatype float\n16.sgpa7: Semester Grade Point Average of seventh semester, datatype float\n17.sgpa8: Semester Grade Point Average of eighth semester, datatype float\n18.cgpa: Cumulative Grade Point Average, datatype float\n19.subjects: comma-separated list of names of subjects enrolled by students, datatype varchar \n\nI have a sql database table as described above which consists of given columns and my query is 'Infrom to all students of Power Electronics subject to attend today's session.', for this create a simple SELECT sql query to get id and roll_no of all students who satisfies criteria given in query and also extract the message in query. Relpy in following format:\nSQL Query:\n {query here} \nMessage : {message}