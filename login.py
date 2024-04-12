from getpass import getpass
import sqlite3
import main
import inform
import requests
import json

gen_url = 'http://localhost:11434/api/generate'


def categorize_query(ID, query):
    # query = "give me list of students enrolled for Data Structures subject"
    data = {
    "model": "gemma",
    "prompt":"Categorize following query, if following query is to inform or it is a notice then category is 'inform' else if following query is to retrive data then category is 'retrive'.\nQuery : '"+query+"'. Relpy in following format:\nCategory: {category}",
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

    # if resp:
    #     return resp['response']
    # else:
    #     None
    
    if resp['response'].find("inform") != -1 or resp['response'].find("Inform") != -1:
        print("Sure! Let me inform you about...")
        inform.main(ID, prompt)
    elif resp['response'].find("retrieve") != -1 or resp['response'].find("Retrieve") != -1:
        print("Okay! Here is what I found.")
        main.main(prompt)
    else:
        print("Unknown category : ", resp['response'])


def main(ID):
    sql = f'''SELECT * 
                FROM notices 
                WHERE ? IN (SELECT CAST(receiver_ids AS INTEGER) FROM notices)'''
    try:
        print("in try....................")
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        rows = cursor.execute(sql, (ID,)).fetchall()
        conn.close()

        print("Fetch success...........................")
        resp_list = []

        print("\nToday's updates for you : \n")
        print("Rows............ :::::::::: ", len(rows))
        if len(rows) > 0:
            print("Iterating.........................")
            for row in rows:
                # print(row[3][2:-1])
                # print("Msg by : ", row[1])
                # print("\n")
                resp_list.append(row[3][2:-1]+"\nMsg by: "+ str(row[1]))
                # print(resp_list)
            return json.dumps(resp_list)
        else:
            print("Else block.......................................")
            return "not"
        
    except Exception as e:
        print("Exception:::::::::::::::::::: ", e)
        return "not"



if __name__ == "__main__":
    print("Hey, I'm Lana here.\nPlease login first with your ID. : ")


        

