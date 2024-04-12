cat = """
**Category:** Retrieve

The query requests a list of students enrolled for the Data Structures subject. This is a request to retrieve data from a database or other data source.
"""

if cat.find("inform") != -1 or cat.find("Inform") != -1:
    print("Sure! Let me inform you about...")

elif cat.find("retrieve") != -1 or cat.find("Retrieve") != -1:
    print("Okay! Here is what I found.")

else:
    print("Unknown category : ", cat)
