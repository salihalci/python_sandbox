
import sqlite3
#save questions to db
def savequestion(question,answer):
    print("save question started")
    try: 
        with sqlite3.connect("memorycards.db") as con:
            cur =con.cursor()
            index = cur.execute("SELECT max(id) from questions").fetchall()
            
            if index[0][0] ==None: # if table is empty returns None
                indexcount=1
            else:
                indexcount = index[0][0] +1
            
            
            cur.execute("INSERT INTO questions (id,question,answer) values(?,?,?)",(indexcount,question,answer))
            con.commit
            print("Record created!")
            msg="Record created"
    except:
        con.rollback()
    finally:
        con.close()


def retrieveQuestions():
    print("retrieve questions started")
