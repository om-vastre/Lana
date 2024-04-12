import requests
import sqlite3
from tabulate import tabulate

gen_url = 'http://localhost:11434/api/generate'

def create_query(query):
    # query = "give me list of students enrolled for Data Structures subject"

    data = {
    "model": "gemma",
    "prompt":"Table name : students\nColumns & Column info :\n1. id : id of student user, datatype int\n2.roll_no: Roll no of students, datatype int\n3.name: Name of student, datatype varchar\n4.division: division of student, datatype varchar\n5.year: year of study, datatype int\n6.department : engineering department of students, datatype varchar\n7.mobileno: mobile no of student, datatype varchar\n8.email: email id of students, datatype varchar\n9.attendance_percentage: attendance in percentage, datatype float\n10. sgpa1: Semester Grade Point Average of first semester, datatype float\n11. sgpa2: Semester Grade Point Average of second semester, datatype float\n12.sgpa3: Semester Grade Point Average of third semester, datatype float\n13.sgpa4: Semester Grade Point Average of fourth semester, datatype float\n14.sgpa5: Semester Grade Point Average of fifth semester, datatype float\n15.sgpa6: Semester Grade Point Average of sixth semester, datatype float\n16.sgpa7: Semester Grade Point Average of seventh semester, datatype float\n17.sgpa8: Semester Grade Point Average of eighth semester, datatype float\n18.cgpa: Cumulative Grade Point Average, datatype float\n19.subjects: comma-separated list of names of subjects enrolled by students, datatype varchar \nI have a sql database table as described above which consists of given columns and my query is '"+query+"', for this create a simple SELECT sql query.\nNote: if select all columns in table in select query if only indetail info is requested in query else only select name & roll_no column.\nReply with only a sql query.",
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
    text = text[text.find("```sql")+6:]
    text = text[:text.find("```")]
    if text[0]==" ":
        text = text[1:]

    if text:
        print("\n\nExtracted SQL Query: ")
        print(text)
        return text
    else:
        return None


def retrive_info(extracted_query):
    if extracted_query:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        rows = cursor.execute(extracted_query).fetchall()
        for row in rows:
            print(row)
        connection.close()
        return rows
    else:
        print("No SQL query found in the input text.")


def draft_msg(rows):
    # rows_str = ""
    # for row in rows:
    #     rows_str += str(row) + "\n"
    # data = {
    # "model": "gemma",
    # "prompt":"Draft following data in table format and respond in following format\nFormat :\n'Following is the data in table format: \n{generated_table}'\nData to convert into table:\n"+rows_str,
    # "stream": False,
    # "options": {
    #     "num_ctx" : 4196,
    #     "num_gpu" : 42
    #     }
    # }

    # x = requests.post(gen_url, json = data)
    # resp = x.json()
    # print("\n\nTable Data:")
    # print(resp['response'])

    # if resp:
    #     return resp['response']
    # else:
    #     None

    print(tabulate(rows, tablefmt="grid"))


def main(prompt):
    # responce = create_query("give me list of students having cgpa > 6.5")
    responce = create_query(prompt)

    if responce != None:
        extracted_query = extract_sql_query(responce)
        if extracted_query != None:
            rows = retrive_info(extracted_query)
            final_responce = draft_msg(rows)
        else:
            print("Error : Query not found in responce!!")
    else:
        print("Error : Model failed to generate responce!!")


if __name__  == "__main__":
    print("running this file")