import requests



gen_url = 'http://localhost:11434/api/generate'
query = "give me list of students enrolled for Data Structures subject"
data = {
"model": "gemma",
"prompt":"Table name : students\nColumns & Column info :\n1. id : id of student user, datatype int\n2.roll_no: Roll no of students, datatype int\n3.name: Name of student, datatype varchar\n4.division: division of student, datatype varchar\n5.year: year of study, datatype int\n6.department : engineering department of students, datatype varchar\n7.mobileno: mobile no of student, datatype varchar\n8.email: email id of students, datatype varchar\n9.attendance_percentage: attendance in percentage, datatype float\n10. sgpa1: Semester Grade Point Average of first semester, datatype float\n11. sgpa2: Semester Grade Point Average of second semester, datatype float\n12.sgpa3: Semester Grade Point Average of third semester, datatype float\n13.sgpa4: Semester Grade Point Average of fourth semester, datatype float\n14.sgpa5: Semester Grade Point Average of fifth semester, datatype float\n15.sgpa6: Semester Grade Point Average of sixth semester, datatype float\n16.sgpa7: Semester Grade Point Average of seventh semester, datatype float\n17.sgpa8: Semester Grade Point Average of eighth semester, datatype float\n18.cgpa: Cumulative Grade Point Average, datatype float\n19.subjects: comma-separated list of names of subjects enrolled by students, datatype varchar \n\nI have a sqlite3 database table as described above which consists of given columns and my query is '"+query+"', for this create a simple SELECT sqlite3 query to get id and roll_no of all students who satisfies criteria given in query and also extract the message in query. Relpy in following format:\nsqlite3 Query:\n {query} \nMessage : {message}",
"stream": False,
"options": {
    "num_gpu" : 2
    }
}

x = requests.post(gen_url, json = data)
resp = x.json()
print(resp['response'])

if resp:
    print(resp['response'])
else:
    print("else block")