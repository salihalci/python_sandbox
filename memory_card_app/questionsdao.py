
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
    
    try:
        with sqlite3.connect("memorycards.db") as con:
            cur = con.cursor()
            questions = cur.execute("SELECT id,question,answer FROM questions").fetchall()
            print(type(questions))
    except:
        pass
    finally:
        con.close()
        return questions
    
def retrieveQuestion(id):
    print("retrieve question started")
    
    try:
        with sqlite3.connect("memorycards.db") as con:
            cur = con.cursor()
            question = cur.execute("SELECT id,question,answer FROM questions where id=?",(id,)).fetchall()
            
    except:
        pass
    finally:
        con.close()
        return question


def deleteQuestion(id):
    print("delete question started")
    msg=""
    try:
        with sqlite3.connect("memorycards.db") as con:
            cur = con.cursor()
            question = cur.execute("DELETE FROM questions where id=?",(id,))
            con.commit
            msg=f" Record deleted. id is {id}"
    except Exception as err:
        con.rollback()
        print(err)
        msg="An error occured during delete operation."
        pass
    finally:
        con.close()
        return msg



def updateQuestion(id,question,answer):

    print("update question started")
    print(f"{id},{question} {answer}")
    msg="update"
    try:
        with sqlite3.connect("memorycards.db") as con:
            cur = con.cursor()
            question = cur.execute("UPDATE questions SET question =?, answer=? where id=?",(question,answer,id))
            con.commit()
            msg="Record updated"
    except Exception as er:
        print(er)
        con.rollback()
        msg="Error occured"
    finally:
        con.close()
        return msg

