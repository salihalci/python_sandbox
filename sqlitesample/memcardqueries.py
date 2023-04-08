import sqlite3
def retrieveAll():
    conn= sqlite3.connect("memorycards.db")
    c = conn.cursor()
    c.execute("SELECT  rowid,* FROM questions")
    #c.fetchone()
    #c.fetchmany(3)
    #c.fetchall()

    #print(c.fetchall())

    items = c.fetchall()
    for x in items:
        print(f"{x[0]} Question {x[1]} ")

        for x in items:
            print(x)

    conn.commit()
    conn.close()


def add_memorycard(id,question,answer):
    """Function impelentation of insert operation"""
    conn = sqlite3.connect('memorycards.db')
    curs = conn.cursor()

    curs.execute("INSERT INTO QUESTIONS VALUES(?,?,?)",(id,question,answer))
    print("Record inserted!")
    conn.commit()
    conn.close()

add_memorycard(29,"SampleQuestion","SampleAnswer")

def delete_memorycard(id):
    conn =sqlite3.connect('memorycards.db')
    curs=conn.cursor()

    curs.execute("DELETE FROM QUESTIONS WHERE id = (?)",[id]) #need an array to pass önemli

    conn.commit()
    conn.close()

delete_memorycard('29')
retrieveAll()

def addmany_memorycards(card_list):

    conn = sqlite3.connect('memorycards.db')
    curs =conn.cursor()
    query = "INSERT INTO questions(id, question, answer) VALUES (?, ?, ?)"
    curs.executemany(query, card_list)
    print("Records added")
    conn.commit()
    conn.close()


cardList = [
    ('40','SampleQuestion','SampleAnswer'),
    ('41','SampleQuestio1','SampleAnswer1')
]

addmany_memorycards(cardList)

retrieveAll()
